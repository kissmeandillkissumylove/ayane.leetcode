from typing import List


class Solution:
	@staticmethod
	def removeElement(nums: List[int], val: int) -> int:
		try:
			while True:
				nums.remove(val)
		except ValueError:
			return len(nums)
