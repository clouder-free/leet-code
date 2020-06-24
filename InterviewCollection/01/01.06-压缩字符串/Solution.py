#! /usr/bin/python

class Solution(object):

	def compressString(self, S: str) -> str:
		if not S:
			return ""
		if len(S) == 1:
			return S
		result = ""
		i, cnt = 1, 1
		while i < len(S):
			if S[i] == S[i-1]:
				cnt += 1
			else:
				result += S[i-1] + str(cnt)
				cnt = 1
			i += 1
		result += S[i-1] + str(cnt)
		if len(result) < len(S):
			return result
		else:
			return S

def main():
	# S = "aabcccccaaa"
	S = "abbccd"
	solution = Solution()
	result = solution.compressString(S=S)
	print(result)

# 输入："aabcccccaaa"
# 输出："a2b1c5a3"
# 输入："abbccd"
# 输出："abbccd"
# 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。

if __name__ == "__main__":
	main()

