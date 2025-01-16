import unittest
import pandas as pd
from modules.data_processing import load_data, combine_data

class TestDataProcessing(unittest.TestCase):
    def test_load_data(self):
        data = load_data("data/sample_data.csv")
        self.assertFalse(data.empty)

    def test_combine_data(self):
        df1 = pd.DataFrame({"col1": [1, 2]})
        df2 = pd.DataFrame({"col1": [3, 4]})
        combined = combine_data(df1, df2)
        self.assertEqual(len(combined), 4)

if __name__ == "__main__":
    unittest.main()
