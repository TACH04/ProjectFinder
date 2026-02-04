#!/usr/bin/env python3
"""
Test script for Gmail OAuth email sending
Sends a test email using the OAuth2 credentials from token.json
"""

import os.path
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build
import logging

# Set up logging
logging.basicConfig(
    filename='email_test.log', 
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

# Scopes required for sending email
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Email configuration
SENDER_EMAIL = "projectfinderinfo@gmail.com"
RECEIVER_EMAIL = "tanner.hochberg@gmail.com"


def get_gmail_service():
    """Get authenticated Gmail API service"""
    creds = None
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(current_dir, 'token.json')
    creds_path = os.path.join(current_dir, 'credentials.json')


    print(f"  📂 Looking for token at: {token_path}")
    logging.info(f"Looking for token at: {token_path}")
    print(f"  📂 Looking for credentials at: {creds_path}")
    logging.info(f"Looking for credentials at: {creds_path}")

    # Check for existing token
    if os.path.exists(token_path):
        try:
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
            print(f"  ℹ Token found. Valid: {creds.valid}, Expired: {creds.expired}")
            logging.info(f"Token found. Valid: {creds.valid}, Expired: {creds.expired}")
        except Exception as e:
            print(f"  ⚠ Error loading token.json: {e}")
            logging.error(f"Error loading token.json: {e}")
    else:
        print("  ℹ No token.json found")
        logging.info("No token.json found")
    
    # If no valid credentials, authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("  🔄 Refreshing expired token...")
            try:
                creds.refresh(Request())
                # Save the refreshed credentials
                with open(token_path, 'w') as token:
                    token.write(creds.to_json())
                print("  ✅ Token refreshed and saved.")
            except Exception as e:
                print(f"  ⚠ Failed to refresh token: {e}")
                creds = None # Force re-auth

        if not creds or not creds.valid:

            if not os.path.exists(creds_path):
                print(f"  ❌ Error: credentials.json not found at {creds_path}")
                logging.error(f"Error: credentials.json not found at {creds_path}")
                print("  Contents of directory:")
                logging.info("Contents of directory:")
                for f in os.listdir(current_dir):
                    print(f"    - {f}")
                    logging.info(f"    - {f}")
                return None
            
            print("  🔐 Starting OAuth flow...")
            logging.info("Starting OAuth flow...")
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
            
            # Save the credentials
            with open(token_path, 'w') as token:
                token.write(creds.to_json())
                print("  ✅ New token saved!")

    
    return build('gmail', 'v1', credentials=creds)


def create_test_email():
    """Create a test email message"""
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = f"🧪 ProjectFinder Test Email - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .header {{ background-color: #27ae60; color: white; padding: 20px; text-align: center; border-radius: 5px 5px 0 0; }}
            .content {{ padding: 20px; border: 1px solid #ddd; border-top: none; border-radius: 0 0 5px 5px; background-color: #f9f9f9; }}
            .success {{ color: #27ae60; font-weight: bold; }}
            .footer {{ margin-top: 20px; font-size: 12px; color: #95a5a6; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h2>✅ ProjectFinder Email Test</h2>
        </div>
        
        <div class="content">
            <p class="success">🎉 If you're reading this, your OAuth email setup is working!</p>
            
            <p><strong>Test Details:</strong></p>
            <ul>
                <li><strong>Sent at:</strong> {datetime.now().strftime('%A, %B %d, %Y at %I:%M:%S %p')}</li>
                <li><strong>From:</strong> {SENDER_EMAIL}</li>
                <li><strong>To:</strong> {RECEIVER_EMAIL}</li>
                <li><strong>Method:</strong> Gmail API with OAuth2</li>
            </ul>
            
            <p>Your ProjectFinder notification system is ready to send alerts when new projects are detected!</p>
            
            <div class="footer">
                <p>This is an automated test message from ProjectFinder</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    msg.attach(MIMEText(html_content, 'html'))
    return msg


def send_test_email():
    """Send a test email using Gmail API with OAuth"""
    print("\n📧 ProjectFinder Email Test")
    print("=" * 40)
    print(f"From: {SENDER_EMAIL}")
    print(f"To:   {RECEIVER_EMAIL}")
    print("=" * 40)
    
    # Get Gmail service
    print("\n🔑 Authenticating with Gmail API...")
    service = get_gmail_service()
    
    if not service:
        print("❌ Failed to authenticate with Gmail API")
        return False
    
    print("✅ Authentication successful!")
    
    # Create and send email
    print("\n📝 Creating test email...")
    message = create_test_email()
    
    # Encode the message
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    

    
    try:
        print("📤 Sending email...")
        logging.info("Sending email...")
        result = service.users().messages().send(
            userId='me',
            body={'raw': raw_message}
        ).execute()
        
        print(f"\n✅ SUCCESS! Email sent!")
        logging.info("SUCCESS! Email sent!")
        print(f"   Message ID: {result.get('id')}")
        logging.info(f"Message ID: {result.get('id')}")
        print(f"\n📬 Check {RECEIVER_EMAIL} for the test email!")
        return True
        
    except Exception as e:
        print(f"\n❌ Failed to send email: {e}")
        logging.error(f"Failed to send email: {e}")
        return False


if __name__ == '__main__':
    send_test_email()
