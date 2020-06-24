#! /usr/bin/python

class Solution(object):

	def isFlipedString(self, s1: str, s2: str) -> bool:
		if not s1 and not s2:
			return True
		if len(s1) != len(s2) or s1 == s2:
			return False
		for i in range(len(s1)):
			if s1[i+1:] + s1[:i+1] == s2:
				return True
		else:
			return False

def main():
	s1 = "a"
	s2 = "a"
	solution = Solution()
	result = solution.isFlipedString(s1=s1, s2=s2)
	print(result)

if __name__ == "__main__":
	main()
