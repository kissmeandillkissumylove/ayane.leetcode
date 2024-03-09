from code.code._1_Two_Sum import Solution
from unittest import TestCase, main


class TestTwo_Sum1(TestCase):
	def test_twoSum(self):
		self.assertEqual(Solution.twoSum([2,7,11,15], 9), [0, 1])
		self.assertEqual(Solution.twoSum([3,2,4], 6), [1,2])
		self.assertEqual(Solution.twoSum([3,3], 6), [0, 1])

if __name__ == "__main__":
	main()
