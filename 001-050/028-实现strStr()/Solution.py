#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
"""

class Solution(object):

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        i = 0
        while i+len(needle) <= len(haystack):
            if needle == haystack[i:i+len(needle)]:
                return i
            i += 1
        return -1


def main():
    haystack = "aaaaa"
    needle = "bba"
    solution = Solution()
    result = solution.strStr(haystack=haystack, needle=needle)
    print(result)

if __name__ == "__main__":
    main()

"""
输入: haystack = "hello", needle = "ll" 输出: 2
输入: haystack = "aaaaa", needle = "bba" 输出: -1
"""
