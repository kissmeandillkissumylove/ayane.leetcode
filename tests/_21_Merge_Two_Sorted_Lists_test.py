from code.code._21_Merge_Two_Sorted_Lists import ListNode, Solution
from unittest import TestCase, main


class TestListNode(TestCase):
	test_list = ListNode()

	def test_append(self):
		self.assertIsNone(self.test_list.append(0))
		self.assertIsNone(self.test_list.append(1))
		self.assertEqual(self.test_list.append(10), None)

	def test_get_list(self):
		self.assertEqual(self.test_list.get_list(), [0, 1, 10])
		# linked list test with 1000 elements
		self.test_list = ListNode()
		for elt in range(0, 1000):
			self.test_list.append(elt)
		self.assertEqual(self.test_list.get_list(), [elt for elt in range(0, 1000)])


class TestSolution(TestCase):

	def test_mergeTwoLists(self):
		list1 = ListNode()
		list2 = ListNode()
		for elt in [1, 3, 5, 7, 9]:
			list1.append(elt)
		for elt in [0, 2, 4, 6, 8, 10]:
			list2.append(elt)
		result = Solution.mergeTwoLists(list1, list2)
		self.assertEqual(result.get_list(), [0, 2, 4, 6, 8, 10])
		self.assertNotEqual(result.get_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == "__main__":
	main()
