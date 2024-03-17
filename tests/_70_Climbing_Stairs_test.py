from code.code._70_Climbing_Stairs import Solution
import unittest


class TestSolution(unittest.TestCase):
	def test_climbStairs(self):
		self.assertEqual(Solution.climbStairs(1), 1)
		self.assertEqual(Solution.climbStairs(2), 2)
		self.assertEqual(Solution.climbStairs(3), 3)
		self.assertEqual(Solution.climbStairs(4), 5)
		self.assertEqual(Solution.climbStairs(8), 34)
		self.assertEqual(Solution.climbStairs(25), 121393)

	def test_climbStairs_NotEqual(self):
		self.assertNotEqual(Solution.climbStairs(4), 4)


if __name__ == '__main__':
	unittest.main()
