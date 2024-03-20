from code.code._83_Remove_Duplicates_from_Sorted_List import Solution
from code.code.singly_linked_list import ListNode
import unittest


class TestSolution(unittest.TestCase):
	def test_deleteDuplicates(self):
		array = ListNode()
		test_list = [1, 1, 2, 3, 3]
		for _ in test_list:
			array.append(_)

		self.assertEqual(array.get_list(), test_list)
		self.assertEqual(Solution.deleteDuplicates(array.get_root()), array.get_root())
		self.assertEqual(array.get_list(), [1, 2, 3])

		array = ListNode()
		test_list = [1, 1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
		for _ in test_list:
			array.append(_)

		self.assertEqual(array.get_list(), test_list)
		self.assertEqual(Solution.deleteDuplicates(array.get_root()), array.get_root())
		self.assertEqual(array.get_list(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

	def test_deleteDuplicates_NotEquals(self):
		array = ListNode()
		test_list = [1, 1, 2, 3, 3]
		for _ in test_list:
			array.append(_)

		self.assertEqual(array.get_list(), test_list)
		self.assertEqual(Solution.deleteDuplicates(array.get_root()), array.get_root())
		self.assertNotEqual(array.get_list(), test_list)

		array = ListNode()
		test_list = [1, 1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
		for _ in test_list:
			array.append(_)

		self.assertEqual(array.get_list(), test_list)
		self.assertEqual(Solution.deleteDuplicates(array.get_root()), array.get_root())
		self.assertNotEqual(array.get_list(), test_list)


if __name__ == '__main__':
	unittest.main()
