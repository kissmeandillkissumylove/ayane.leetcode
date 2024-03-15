from typing import List


class Solution:
	@staticmethod
	def plusOne(digits: List[int]) -> List[int]:
		num = int(''.join(map(str, digits))) + 1
		return [int(i) for i in str(num)]
