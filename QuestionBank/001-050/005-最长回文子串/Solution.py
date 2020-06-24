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

def main():
    s = "35534321"
    solution = Solution()
    string = solution.longestPalindrome(s=s)
    print(string)

if __name__ == "__main__":
    main()
