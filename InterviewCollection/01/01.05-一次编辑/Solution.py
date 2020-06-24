#! /usr/bin/python

class Solution(object):

	def oneEditAway(self, first: str, second: str) -> bool:
		lf = len(first)
		ls = len(second)
		# 替换
		if lf == ls:
			i = 0
			while i < lf:
				if first[i] != second[i]:
					break
				i += 1
			return first[i+1:] == second[i+1:]
		# 删除/添加
		elif abs(lf - ls) == 1:
			i = 0
			while i < min(lf, ls):
				if first[i] != second[i]:
					break
				i += 1
			# 删除
			if lf > ls:
				return first[i+1:] == second[i:]
			# 添加
			else:
				return first[i:] == second[i+1:]
		return False


def main():
	first = "pales"
	second = "pal"
	solution = Solution()
	result = solution.oneEditAway(first=first, second=second)
	print(result)

if __name__ == "__main__":
	main()
