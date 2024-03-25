from code.code._94_Binary_Tree_Inorder_Traversal import Solution
from code.code.binary_tree import BinaryTree
import unittest


class TestSolution(unittest.TestCase):
	def test_inorderTraversal(self):
		_, tree = [1, 0, 2, 3], BinaryTree()
		for _ in _:
			tree.add(_)
		self.assertEqual(Solution.inorderTraversal(tree.root), [0, 1, 2, 3])

		_, tree = [], BinaryTree()
		for _ in _:
			tree.add(_)
		self.assertEqual(Solution.inorderTraversal(tree.root), [])

		_, tree = [1], BinaryTree()
		for _ in _:
			tree.add(_)
		self.assertEqual(Solution.inorderTraversal(tree.root), [1])


if __name__ == '__main__':
	unittest.main()
