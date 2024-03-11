from code.code._27_Remove_Element import Solution
import unittest


class TestSolution(unittest.TestCase):
	test_list = []

	def test_something(self):
		self.test_list = [3, 2, 2, 3]
		self.assertEqual(Solution.removeElement(self.test_list, 3), 2)
		self.assertEqual(self.test_list, [2, 2])
		# one more test
		self.test_list = [0, 1, 2, 2, 3, 0, 4, 2]
		self.assertEqual(Solution.removeElement(self.test_list, 2), 5)
		self.assertEqual(self.test_list, [0, 1, 3, 0, 4])


if __name__ == '__main__':
	unittest.main()
