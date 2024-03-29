from code.code._9_Palindrome_Number import Solution
from unittest import TestCase, main


class TestSolution(TestCase):
	def test_singleNumber(self):
		self.assertEqual(Solution.isPalindrome(121), True)
		self.assertEqual(Solution.isPalindrome(-121), False)
		self.assertEqual(Solution.isPalindrome(10), False)


if __name__ == "__main__":
	main()
