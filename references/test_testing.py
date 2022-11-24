# Reference: https://docs.python.org/3/library/unittest.html
# Usage: 
#   python test_testing.py
#   python -m unittest
#   # Verbose:
#   python -m unittest -v

import unittest
from unittest.mock import Mock, patch

import testing
import pandas as pd


def read_csv_side_effect(fp: str) -> pd.DataFrame:
	return pd.DataFrame({"x": [1], "y": [1]})


class Test(unittest.TestCase):

	def test_add_one(self):
		x = 1
		exp = 2
		obs = testing.add_one(x)
		self.assertTrue(isinstance(obs, int))
		self.assertEqual(obs, exp)


	def test_add_one_type_error(self):
		x = "1"
		with self.assertRaises(TypeError):
			testing.add_one(x)


	@patch("testing.pd.read_csv", autospec=True)
	def test_read_file(self, mock_read_csv: Mock):
		mock_read_csv.side_effect = read_csv_side_effect
		obs = testing.read_file("data.csv")
		exp = pd.DataFrame({"x": [1], "y": [1]})
		pd.testing.assert_frame_equal(obs, exp)


if __name__ == "__main__":
	unittest.main()
