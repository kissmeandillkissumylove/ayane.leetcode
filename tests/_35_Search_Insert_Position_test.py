from code.code._35_Search_Insert_Position import Solution
import unittest


class TestSolution(unittest.TestCase):
	def test_searchInsert(self):
		self.assertEqual(Solution.searchInsert([1, 3, 5, 6], 5), 2)
		self.assertEqual(Solution.searchInsert([1, 3, 5, 6], 2), 1)
		self.assertEqual(Solution.searchInsert([1, 3, 5, 6], 7), 4)


if __name__ == "__main__":
	unittest.main()
