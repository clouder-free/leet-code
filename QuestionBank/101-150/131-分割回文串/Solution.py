#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):

    def partition(self, s: str) -> [[str]]:
        result = []
        if not s:
            return result

        def reverse(s, index, t, result):
            if index == len(s):
                result.append(t[:])
                return
            for i in range(index + 1, len(s) + 1):
                if s[index:i] == s[index:i][::-1]:
                    t.append(s[index:i])
                    reverse(s, i, t, result)
                    t.pop()
        reverse(s, 0, [], result)
        return result

def main():
    s = "aab"
    solution = Solution()
    result = solution.partition(s=s)
    print(result)

if __name__ == "__main__":
    main()
