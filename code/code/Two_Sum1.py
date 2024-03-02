from typing import List


class Solution:
	@staticmethod
	def twoSum(nums: List[int], target: int) -> List[int]:
		map = {}
		len_nums = len(nums)
		for elt in range(0, len_nums):
			map[nums[elt]] = elt
		for elt in range(0, len_nums):
			find = target - nums[elt]
			if find in map and map[find] != elt:
				return [elt, map[find]]
		return []
