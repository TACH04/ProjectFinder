
import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# 1. Setup paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 2. Define Mock Objects *BEFORE* importing source code
class MockPortalScrapingError(Exception):
    pass

# Mock the scraper module completely so NO real code runs
mock_scraper_module = MagicMock()
mock_scraper_module.PortalScrapingError = MockPortalScrapingError
mock_scraper_module.OpenGovScraper = MagicMock()

# Mock config
mock_config = MagicMock()
mock_config.PORTALS = {"phoenix": {"name": "Test Portal", "url": "http://test"}}
mock_config.BROWSER_SETTINGS = {"headless": True}
mock_config.EMAIL_CONFIG = {"enabled": False}

# 3. Patch sys.modules to inject our mocks
modules_to_patch = {
    'scraper.scraper': mock_scraper_module,
    'scraper.browser': MagicMock(),
    'scraper.email_notifier': MagicMock(),
    'config': mock_config,
    'google.oauth2': MagicMock(),
    'google.auth.transport.requests': MagicMock(),
}

with patch.dict('sys.modules', modules_to_patch):
    import run_scraper

class TestRetryLogic(unittest.TestCase):
    def test_retry_success_after_failure(self):
        """Test that scraper retries 3 times when PortalScrapingError is raised"""
        
        # Access the mock class that was injected into run_scraper
        mock_scraper_class = mock_scraper_module.OpenGovScraper
        mock_scraper_instance = mock_scraper_class.return_value
        
        # Configure side effects: Fail 2 times, Succeed 1 time
        mock_scraper_instance.scrape_portal.side_effect = [
            MockPortalScrapingError("Simulated Cloudflare Timeout"),
            MockPortalScrapingError("Simulated Network Error"),
            [MagicMock(title="Success Project", portal="phoenix")]
        ]
        
        # Patch other calls in run_scraper to keep output clean
        with patch('run_scraper.check_for_new_projects', return_value=([], [])), \
             patch('run_scraper.send_email_notification'), \
             patch('time.sleep') as mock_sleep:
            
            print("\n--- Starting Retry Logic Verification -------------------")
            run_scraper.main()
            print("---------------------------------------------------------")
            
            # Assertions
            self.assertEqual(mock_scraper_instance.scrape_portal.call_count, 3, "Should have retried 3 times")
            self.assertEqual(mock_sleep.call_count, 2, "Should have slept (backed off) 2 times")

if __name__ == '__main__':
    unittest.main()
