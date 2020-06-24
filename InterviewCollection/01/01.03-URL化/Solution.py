#! /usr/bin/python

class Solution(object):

	def replaceSpaces(self, S: str, length: int) -> str:
		s = S[:length]
		return s.replace(" ", "%20")

def main():
	# S = "Mr John Smith    "
	# length = 13
	S = "               "
	length = 5
	solution = Solution()
	result = solution.replaceSpaces(S=S, length=length)
	print(result)

if __name__ == "__main__":
	main()

"""
输入："", 13
输出："Mr%20John%20Smith"

输入："               ", 5
输出："%20%20%20%20%20"
"""

