class Solution:
	@staticmethod
	def isPalindrome(x: int) -> bool:
		line = str(x)
		return line == line[::-1]
