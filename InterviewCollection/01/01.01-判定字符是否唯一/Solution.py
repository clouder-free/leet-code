#! /usr/bin/python

class Solution(object):

	def isUnique(self, astr: str) -> bool:
		return len(set(astr)) == len(astr)

def main():
	astr = "abc"
	solution = Solution()
	result = solution.isUnique(astr=astr)
	print(result)

if __name__ == "__main__":
	main()

