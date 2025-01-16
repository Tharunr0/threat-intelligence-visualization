import unittest
import pandas as pd
from modules.threat_analysis import analyze_threats

class TestThreatAnalysis(unittest.TestCase):
    def test_analyze_threats(self):
        # Create a mock dataset
        mock_data = pd.DataFrame({
            "id": [1, 2, 3, 4],
            "category": ["Phishing", "Malware", "Ransomware", "Phishing"],
            "threat_level": ["High", "Medium", "High", "Low"]
        })

        high_risk = analyze_threats(mock_data)
        self.assertIsInstance(high_risk, pd.DataFrame)
        self.assertEqual(len(high_risk), 2)  # Only two "High" threat levels

        # Validate the data is filtered correctly
        self.assertTrue(all(high_risk["threat_level"] == "High"))

if __name__ == "__main__":
    unittest.main()
