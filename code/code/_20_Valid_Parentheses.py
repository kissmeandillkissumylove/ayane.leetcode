class Solution:
	@staticmethod
	def isValid(s: str) -> bool:
		if len(s) % 2 != 0:
			return False
		dic, tmp = {
			"{": "}", "[": "]", "(": ")"
		}, ""
		for elt in s:
			if elt not in dic:
				try:
					if dic[tmp[-1]] != elt:
						return False
					else:
						tmp = tmp[:-1]
						continue
				except IndexError:
					return False
			tmp += elt
		return True if tmp == "" else False
