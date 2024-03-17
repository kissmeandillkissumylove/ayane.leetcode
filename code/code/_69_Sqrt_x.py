class Solution:
	@staticmethod
	def mySqrt(x: int) -> int:
		# for x < 2
		if x < 1:
			return 0
		if x < 2:
			return 1
		# considering the equation values
		y = x
		z = (y + (x / y)) / 2
		# as we want to get up to 1 decimal digits, the absolute difference should
		# not exceed 0.1
		while abs(y - z) >= 0.1:
			y = z
			z = (y + (x / y)) / 2
		return int(z)
