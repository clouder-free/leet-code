#! /usr/bin/python

class Solution(object):

	def canPermutePalindrome(self, s: str) -> bool:
		from collections import Counter
		cnt = Counter(s)
		numbers = [c for c in cnt.values() if c % 2 != 0]
		return len(numbers) < 2

def main():
	s = "tactcorto"
	solution = Solution()
	result = solution.canPermutePalindrome(s=s)
	print(result)

if __name__ == "__main__":
	main()

