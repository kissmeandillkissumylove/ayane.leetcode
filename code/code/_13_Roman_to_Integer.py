class Solution:
	@staticmethod
	def romanToInt(s: str) -> int:
		map = {
			"I": 1, "V": 5, "X": 10, "L": 50,
			"C": 100, "D": 500, "M": 1000,
		}
		s, ret = s[::-1], 0
		for elt in s:
			if ret == 0:
				ret = map[elt]
			elif tmp <= map[elt]:
				ret = ret + map[elt]
			elif tmp > map[elt]:
				ret = ret - map[elt]
			tmp = map[elt]
		return ret
