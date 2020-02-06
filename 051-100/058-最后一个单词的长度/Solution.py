#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
如果不存在最后一个单词，请返回 0。
说明：一个单词是指仅由字母组成、不包含任何空格的 最大子字符串。
输入: "Hello World"   输出: 5
"""

class Solution(object):

    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        return len(s.split(" ")[-1])

def main():
    s = "hello world  "
    solution = Solution()
    result = solution.lengthOfLastWord(s=s)
    print(result)

if __name__ == "__main__":
    main()
