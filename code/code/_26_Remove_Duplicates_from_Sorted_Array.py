from typing import List


class Solution:
	@staticmethod
	def removeDuplicates(nums: List[int]) -> int:
		new_list = list(set(nums))
		nums.clear()
		for elt in new_list:
			nums.append(elt)
		nums.sort()
		return len(nums)
