from typing import List


def singleNumber(nums: List[int]) -> int:
	return 2 * sum(set(nums)) - sum(nums)
