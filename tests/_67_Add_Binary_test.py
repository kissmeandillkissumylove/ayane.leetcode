from code.code._67_Add_Binary import Solution
import unittest


class TestSolution(unittest.TestCase):
	def test_addBinary(self):
		self.assertEqual(Solution.addBinary("1010", "1011"), "10101")
		self.assertEqual(Solution.addBinary("11", "1"), "100")
		self.assertEqual(Solution.addBinary("1000101", "1011101"), "10100010")


if __name__ == '__main__':
	unittest.main()
