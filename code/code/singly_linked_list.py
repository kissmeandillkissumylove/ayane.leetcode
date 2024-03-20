class ListNode:
	# Definition for singly-linked list.
	_root = None

	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def append(self, data):
		if not self._root:
			self._root = ListNode(data, None)
			return
		node = self._root
		while node.next:
			node = node.next
		node.next = ListNode(data)

	def get_list(self):
		ret = []
		node = self._root
		while node:
			ret.append(node.val)
			node = node.next
		return ret

	def get_root(self):
		return self._root
