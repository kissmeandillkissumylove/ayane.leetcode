class BinaryTree:
	root = None

	class TreeNode:

		def __init__(self, val, left=None, right=None):
			self.val = val
			self.left = left
			self.right = right

	def _search(self, data, node):
		if data == node.val:
			return "node is existing"
		elif data > node.val:
			if node.right:
				self._search(data, node.right)
			else:
				node.right = self.TreeNode(data)
		elif data < node.val:
			if node.left:
				self._search(data, node.left)
			else:
				node.left = self.TreeNode(data)

	def add(self, data):
		if self.root:
			self._search(data, self.root)
		else:
			self.root = self.TreeNode(data)

	def get_tree_values(self):
		result, temp = [], [self.root, ]
		while temp:
			_ = temp.pop()
			result.append(_.val)
			if _.right:
				temp.append(_.right)
			if _.left:
				temp.append(_.left)
		return result
