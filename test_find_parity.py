import unittest
from find_parity import find_outlier

class Testparity(unittest.TestCase):
	def test_values(self):
		self.assertEqual(find_outlier([3,6,8]), 3)

	def test_errors(self):
		self.assertRaises(ValueError,find_outlier,["3"])