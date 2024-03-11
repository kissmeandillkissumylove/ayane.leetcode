from code.code._28_Find_the_Index_of_the_First_Occurrence_in_a_String import Solution
import unittest


class TestSolution(unittest.TestCase):
	def test_strStr(self):
		self.assertEqual(Solution.strStr("sadbutsad", "sad"), 0)
		self.assertEqual(Solution.strStr("leetcode", "leeto"), -1)
		self.assertEqual(Solution.strStr("ssklossklor", "ssklor"), 5)


if __name__ == '__main__':
	unittest.main()
