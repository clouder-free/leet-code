#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

class Solution(object):

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 当前最长无重复子串
        st = ""
        max_length = 0
        for i in range(len(s)):
            print("i:{}".format(s[i]))
            if s[i] not in st:
                st += s[i]
                max_length = max_length if max_length > len(st) else len(st)
            else:
                st = st[st.find(s[i])+1:] + s[i]
            print("st:{}".format(st))
        return max_length

    def lengthOfLongestSubstring2(self, s: str) -> int:
        # 无重复字符的最大位置
        location = {}
        max_len = 0
        start = 0
        for index, c in enumerate(s):
            # 更新子串的起始位置
            if c in location and location[c] >= start:
                start = location[c] + 1
            location[c] = index
            max_len = max_len if max_len > index - start + 1 else index - start + 1
        return max_len

def main():
    s = "pwfebewadg"
    solution = Solution()
    length = solution.lengthOfLongestSubstring2(s=s)
    print(length)

if __name__ == "__main__":
    main()

"""
示例数据
s = 'pwwkew'
s = 'abcabdef'
s = 'abcabcbb'
s = 'pwfebewadg'
"""


