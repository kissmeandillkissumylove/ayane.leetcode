from code.code._136_Single_Number import singleNumber
from unittest import TestCase, main


class TestSolution(TestCase):

	def test_singleNumber(self):
		self.assertEqual(singleNumber([2, 2, 1]), 1)
		self.assertEqual(singleNumber([4, 1, 2, 1, 2]), 4)
		self.assertEqual(singleNumber([1]), 1)


if __name__ == "__main__":
	main()
