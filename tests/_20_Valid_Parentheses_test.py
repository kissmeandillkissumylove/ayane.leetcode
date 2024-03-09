from code.code._20_Valid_Parentheses import Solution
from unittest import TestCase, main


class TestSolution(TestCase):
	def test_singleNumber(self):
		self.assertEqual(Solution.isValid("()"), True)
		self.assertEqual(Solution.isValid("()[]{}"), True)
		self.assertEqual(Solution.isValid("(]"), False)
		self.assertNotEqual(Solution.isValid("()[]{}"), False)
		self.assertNotEqual(Solution.isValid("{()[]{[]}}[]()"), False)


if __name__ == "__main__":
	main()
