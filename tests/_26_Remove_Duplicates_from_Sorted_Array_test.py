import unittest
from code.code._26_Remove_Duplicates_from_Sorted_Array import Solution


class TestSolution(unittest.TestCase):
	def test_removeDuplicates(self):
		test_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
		self.assertEqual(Solution.removeDuplicates(test_list), 5)
		self.assertEqual(test_list, [0, 1, 2, 3, 4])
		self.assertNotEqual(test_list, [0, 1, 1, 2, 3, 4])
		# one more test
		test_list = [0, 0, 0, 2, 2, 2, 5, 6, 7, 8, 9, 10, 10, 10, 11]
		self.assertEqual(Solution.removeDuplicates(test_list), 9)
		self.assertEqual(test_list, [0, 2, 5, 6, 7, 8, 9, 10, 11])
		self.assertNotEqual(test_list, [0, 0, 2, 5, 6, 7, 8, 9, 10, 11])


if __name__ == '__main__':
	unittest.main()
