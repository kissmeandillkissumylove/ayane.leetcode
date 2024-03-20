from typing import List


class Solution:
	@staticmethod
	def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		counter1, counter2 = 0, 0
		while n != 0:
			if nums1[counter1] == 0:
				nums1[counter1] = nums2[counter2]
				counter2 += 1
				counter1 += 1
				n -= 1
			else:
				counter1 += 1
		nums1.sort()
