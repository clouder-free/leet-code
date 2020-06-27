#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
manacher算法
"""

class Solution(object):

    # 中心扩散法
    def longestPalindrome(self, s: str) -> str:
        string = "#" + "#".join(s) + "#"
        max_palindrome = ""
        for i in range(1, len(string)):
            max_string = self.getPalindromeString(i, i, string)
            # print("return:{}".format(max_string))
            max_string = max_string.replace("#", "")
            # print("max_string:{}".format(max_string))
            if len(max_string) > len(max_palindrome):
                max_palindrome = max_string
        return max_palindrome

    def getPalindromeString(self, i, j, string):
        while i > 0 and j < len(string) and string[i] == string[j]:
            i -= 1
            j += 1
        return string[i+1:j]

    # 动态规划DP
    def longestPalindrome2(self, s: str) -> str:
        if not s:
            return ''
        
        dp = [[False] * len(s) for _ in range(len(s))]
        l, r = 0, 0
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    # 对应 aba 或者 aa bb 这种形式的子串
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    # 更改最新长度子串索引
                    if dp[i][j] and r-l < j-i:
                        l, r = i, j
        return s[l:r+1]
    
def main():
    s = "35534321"
    solution = Solution()
    string = solution.longestPalindrome2(s=s)
    print(string)

if __name__ == "__main__":
    main()
