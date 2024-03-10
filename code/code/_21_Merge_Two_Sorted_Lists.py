from typing import Optional, List


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


class Solution:
	@staticmethod
	def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		if list1 is None:
			return list2
		elif list2 is None:
			return list1
		if list1.val >= list2.val:
			ret, tmp1, tmp2 = list2, list2, list1
		else:
			ret, tmp1, tmp2 = list1, list1, list2
		while True:
			if tmp1.next is None and tmp2 is not None:
				tmp1.next = tmp2
				break
			if tmp2.val > tmp1.next.val:
				tmp1 = tmp1.next
			else:
				remember = tmp1.next
				tmp1.next = tmp2
				tmp2 = remember
				tmp1 = tmp1.next
		return ret
