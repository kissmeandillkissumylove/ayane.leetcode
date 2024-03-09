from code.code._14_Longest_Common_Prefix import Solution
from unittest import TestCase, main


class TestSolution(TestCase):
	def test_singleNumber(self):
		self.assertEqual(Solution.longestCommonPrefix(["flower","flow","flight"]), "fl")
		self.assertNotEqual(Solution.longestCommonPrefix(["flower","flow","flight"]), "")
		self.assertEqual(Solution.longestCommonPrefix(["dog","racecar","car"]), "")
		self.assertNotEqual(Solution.longestCommonPrefix(["dog", "racecar", "car"]), "dc")


if __name__ == "__main__":
	main()
