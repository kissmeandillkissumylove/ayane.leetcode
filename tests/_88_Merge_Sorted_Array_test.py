from code.code._88_Merge_Sorted_Array import Solution
import unittest


class TestSolution(unittest.TestCase):
	def test_merge_Equals(self):
		m, n = 3, 3
		nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
		Solution.merge(nums1, m, nums2, n)
		self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

		m, n = 1, 0
		nums1, nums2 = [1], [0]
		Solution.merge(nums1, m, nums2, n)
		self.assertEqual(nums1, [1])


if __name__ == '__main__':
	unittest.main()
