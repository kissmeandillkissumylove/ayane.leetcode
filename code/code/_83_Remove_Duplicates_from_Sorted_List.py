from typing import Optional


class ListNode:
	...


class Solution:
	@staticmethod
	def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
		node = head
		while node:
			if node.next:
				if node.val != node.next.val:
					node = node.next
				else:
					node.next = node.next.next
			else:
				return head
