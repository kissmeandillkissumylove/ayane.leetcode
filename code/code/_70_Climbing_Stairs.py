class Solution:
	@staticmethod
	def climbStairs(n: int, ddc=None) -> int:
		if n <= 2:
			return n
		if ddc is None:
			ddc = {}
		if n not in ddc:
			ddc[n] = Solution.climbStairs(n - 1, ddc) + Solution.climbStairs(n - 2, ddc)
		return ddc[n]
