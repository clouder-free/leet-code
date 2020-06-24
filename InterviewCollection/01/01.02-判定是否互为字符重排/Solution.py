#! /usr/bin/python

class Solution(object):

	def CheckPermutation(self, s1: str, s2: str) -> bool:
		from collections import Counter
		c = Counter(s1)
		c.subtract(s2)
		for k, v in c.items():
			if v != 0:
				return False
		return True

def main():
	s1 = "a"
	s2 = "ab"
	solution = Solution()
	result = solution.CheckPermutation(s1=s1, s2=s2)
	print(result)

if __name__ == "__main__":
	main()
