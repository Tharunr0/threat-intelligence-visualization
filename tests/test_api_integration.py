import unittest
import pandas as pd
from modules.api_integration import fetch_data


class TestAPIIntegration(unittest.TestCase):
    def test_fetch_data_success(self):
        # Mock the API response for testing purposes
        import requests
        from unittest.mock import patch

        mock_response = [
            {"id": 1, "category": "Phishing", "threat_level": "High"},
            {"id": 2, "category": "Malware", "threat_level": "Medium"},
        ]

        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response

            data = fetch_data()
            self.assertIsInstance(data, pd.DataFrame)
            self.assertEqual(len(data), len(mock_response))

    def test_fetch_data_failure(self):
        # Simulate an API failure
        import requests
        from unittest.mock import patch

        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 500
            mock_get.return_value.json.side_effect = Exception("API Failure")

            data = fetch_data()
            self.assertTrue(data.empty)


if __name__ == "__main__":
    unittest.main()
