from code.code.Roman_to_Integer13 import Solution
from unittest import TestCase, main


class TestSolution(TestCase):
	def test_singleNumber(self):
		self.assertEqual(Solution.romanToInt("III"), 3)
		self.assertEqual(Solution.romanToInt("LVIII"), 58)
		self.assertEqual(Solution.romanToInt("MCMXCIV"), 1994)
		self.assertEqual(Solution.romanToInt("CD"), 400)
		self.assertEqual(Solution.romanToInt("MMMD"), 3500)
		self.assertNotEqual(Solution.romanToInt("LVIII"), 56)
		self.assertNotEqual(Solution.romanToInt("LXXX"), 90)
		self.assertNotEqual(Solution.romanToInt("LXXX"), 70)


if __name__ == "__main__":
	main()
