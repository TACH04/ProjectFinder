"""
Email notification system using Gmail API (OAuth2)
"""

import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List, Dict, Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from scraper.base import Project

# Scopes required for sending email
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    """Get authenticated Gmail API service"""
    creds = None
    
    # Paths needed (assuming running from project root)
    # We look for token/credentials in the current working directory (project root)
    token_path = 'token.json'
    creds_path = 'credentials.json'
    
    # Check for existing token
    if os.path.exists(token_path):
        try:
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        except Exception as e:
            print(f"  ⚠ Error loading token.json: {e}")
    
    # If no valid credentials, authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("  🔄 Refreshing expired email token...")
            try:
                creds.refresh(Request())
                # Save the refreshed credentials
                with open(token_path, 'w') as token:
                    token.write(creds.to_json())
            except Exception as e:
                print(f"  ⚠ Failed to refresh token: {e}")
                creds = None
        
        # If still no valid creds, we need to re-auth or fail
        if not creds or not creds.valid:
            if not os.path.exists(creds_path):
                print("  ❌ Error: credentials.json not found! Cannot send email.")
                return None
            
            print("  🔐 Starting Gmail OAuth flow...")
            try:
                flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
                creds = flow.run_local_server(port=0)
                
                # Save the credentials
                with open(token_path, 'w') as token:
                    token.write(creds.to_json())
            except Exception as e:
                print(f"  ❌ OAuth flow failed: {e}")
                return None
    
    try:
        return build('gmail', 'v1', credentials=creds)
    except Exception as e:
        print(f"  ❌ Failed to build Gmail service: {e}")
        return None


def send_email_notification(
    new_projects: List[Project], 
    sender_email: str,
    receiver_email: str,
    sender_password: str = None,  # Kept for backward compatibility but unused
    failed_portals: List[str] = None
) -> bool:
    """
    Send email notification for new projects using Gmail API
    
    Args:
        new_projects: List of projects detected for the first time
        sender_email: Gmail address to send from
        receiver_email: Email address(es) to receive notifications (comma-separated for multiple)
        sender_password: Unused (legacy argument)
        
    Returns:
        bool: True if sent successfully
    """
    if not new_projects and not failed_portals:
        print("  ℹ No new projects or failures to notify about.")
        return False
        
    print(f"  📧 Sending email notification to {receiver_email}...")
    
    # Get Gmail service
    service = get_gmail_service()
    if not service:
        print("  ❌ Could not initialize Gmail service. Email not sent.")
        return False
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # Subject line
    count_new = len(new_projects)
    subject_parts = []
    if count_new > 0:
        subject_parts.append(f"🎯 {count_new} New Project{'s' if count_new != 1 else ''}")
    
    if failed_portals:
        subject_parts.append(f"⚠️ {len(failed_portals)} Failed Portal{'s' if len(failed_portals) != 1 else ''}")
        
    subject = " | ".join(subject_parts) if subject_parts else "ProjectFinder Update"
        
    msg['Subject'] = subject
    
    # Build HTML body - simplified format showing only City and Project Name
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .header {{ background-color: #2c3e50; color: white; padding: 15px; text-align: center; border-radius: 5px 5px 0 0; }}
            .content {{ padding: 20px; border: 1px solid #ddd; border-top: none; border-radius: 0 0 5px 5px; }}
            .project-list {{ list-style: none; padding: 0; margin: 0; }}
            .project-item {{ padding: 12px 0; border-bottom: 1px solid #eee; display: flex; align-items: flex-start; }}
            .project-item:last-child {{ border-bottom: none; }}
            .city {{ font-weight: bold; color: #2c3e50; min-width: 140px; flex-shrink: 0; }}
            .project-name {{ color: #2980b9; text-decoration: none; }}
            a.project-name:hover {{ text-decoration: underline; }}
            .section-title {{ color: #2c3e50; border-bottom: 2px solid #e74c3c; padding-bottom: 5px; margin-bottom: 15px; }}
            .footer {{ margin-top: 20px; font-size: 12px; color: #95a5a6; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h2>ProjectFinder Alert</h2>
            <p>{datetime.now().strftime('%A, %B %d, %Y')}</p>
        </div>
        
        <div class="content">
    """
    
    # Import PORTALS to get city names
    from config import PORTALS
    
    def get_city_name(portal_key: str) -> str:
        """Get the city name from portal config, or use the key as fallback"""
        if portal_key in PORTALS:
            return PORTALS[portal_key].get('name', portal_key.title())
        return portal_key.title()
    
    # Section 1: New Projects (First time seen)
    if new_projects:
        html += f"""
            <h3 class="section-title">🚨 New Projects ({len(new_projects)})</h3>
            <ul class="project-list">
        """
        
        for p in new_projects:
            city_name = get_city_name(p.portal)
            if p.url:
                project_link = f'<a href="{p.url}" class="project-name">{p.title}</a>'
            else:
                project_link = f'<span class="project-name">{p.title}</span>'
            html += f"""
                <li class="project-item">
                    <span class="city">{city_name}</span>
                    {project_link}
                </li>
            """
        
        html += "</ul>"

    # Section 2: Failed Portals
    if failed_portals:
        html += f"""
            <h3 class="section-title" style="border-color: #f1c40f; margin-top: 30px;">⚠️ Skipped Portals ({len(failed_portals)})</h3>
            <p style="font-size: 14px; color: #7f8c8d; margin-bottom: 10px;">The following portals could not be reached or timed out:</p>
            <ul class="project-list">
        """
        
        for p_key in failed_portals:
            city_name = get_city_name(p_key)
            html += f"""
                <li class="project-item">
                    <span class="city" style="color: #e67e22;">{city_name}</span>
                    <span class="project-name" style="color: #95a5a6;">Connection Failed / Timeout</span>
                </li>
            """
        html += "</ul>"
            
    html += """
            <div class="footer">
                <p>Sent automatically by ProjectFinder</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    msg.attach(MIMEText(html, 'html'))
    
    try:
        # Encode message for Gmail API
        raw_message = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf-8')
        
        service.users().messages().send(
            userId='me',
            body={'raw': raw_message}
        ).execute()
        
        print("  ✓ Email notification sent successfully!")
        return True
    except Exception as e:
        print(f"  ✗ Failed to send email: {e}")
        return False
