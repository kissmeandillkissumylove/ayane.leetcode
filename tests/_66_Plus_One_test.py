from code.code._66_Plus_One import Solution
import unittest


class TestSolution(unittest.TestCase):
	def test_plusOne(self):
		self.assertEqual(Solution.plusOne([1, 2, 3]), [1, 2, 4])
		self.assertEqual(Solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
		self.assertEqual(Solution.plusOne([9]), [1, 0])


if __name__ == '__main__':
	unittest.main()
