from typing import List


class Solution:
	@staticmethod
	def searchInsert(nums: List[int], target: int) -> int:
		left, right = 0, len(nums) - 1
		while left <= right:
			middle = (left + right) // 2
			if nums[middle] < target:
				left = middle + 1
			elif nums[middle] > target:
				right = middle - 1
			else:
				return middle
		return left
