from code.code._69_Sqrt_x import Solution
import unittest


class TestSolution(unittest.TestCase):
	def test_mySqrt(self):
		self.assertEqual(Solution.mySqrt(0), 0)
		self.assertEqual(Solution.mySqrt(1), 1)
		self.assertEqual(Solution.mySqrt(2), 1)
		self.assertEqual(Solution.mySqrt(3), 1)
		self.assertEqual(Solution.mySqrt(4), 2)
		self.assertEqual(Solution.mySqrt(10), 3)
		self.assertEqual(Solution.mySqrt(25), 5)
		self.assertEqual(Solution.mySqrt(26), 5)
		self.assertEqual(Solution.mySqrt(1000), 31)

	def test_mySqrt_NotEqual(self):
		self.assertNotEqual(Solution.mySqrt(0), float)
		self.assertNotEqual(Solution.mySqrt(1), float)
		self.assertNotEqual(Solution.mySqrt(2), float)
		self.assertNotEqual(Solution.mySqrt(3), 1.7)


if __name__ == '__main__':
	unittest.main()
