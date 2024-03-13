from code.code._58_Length_of_Last_Word import Solution
import unittest


class TestSolution(unittest.TestCase):
	def test_lengthOfLastWord(self):
		self.assertEqual(Solution.lengthOfLastWord("Hello World"), 5)
		self.assertEqual(Solution.lengthOfLastWord("   fly me   to   the moon  "), 4)
		self.assertEqual(Solution.lengthOfLastWord("luffy is still joyboy"), 6)
		self.assertEqual(Solution.lengthOfLastWord("a"), 1)


if __name__ == '__main__':
	unittest.main()
