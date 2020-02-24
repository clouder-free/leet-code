#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回符合要求的最少分割次数。
示例:
输入: "aab" 输出: 1
解释: 进行一次分割就可将s分割成 ["aa","b"] 这样两个回文子串。
"""

class Solution(object):

    def minCut(self, s: str) -> int:
        judge = [[False] * len(s) for _ in range(len(s))]
        dp = [-1] * len(s)
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i<=1 or judge[i+1][j-1]):
                    judge[i][j] = True
                    if j+1 < len(s):
                        if dp[i] == -1:
                            dp[i] = 1 + dp[j+1]
                        else:
                            dp[i] = min(dp[i], 1 + dp[j+1])
                    else:
                        dp[i] = 0
        return dp[0]

def main():
    s = "aab"
    solution = Solution()
    result = solution.minCut(s=s)
    print(result)

if __name__ == "__main__":
    main()

