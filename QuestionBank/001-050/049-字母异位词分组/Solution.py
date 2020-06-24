#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
"""

class Solution(object):

    def groupAnagrams(self, strs: [str]) -> [[str]]:
        results = {}
        for s in strs:
            converts = list(s)
            converts.sort()
            c = ''.join(converts)
            if c not in results:
                results[c] = []
            results[c].append(s)
        return list(results.values())

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    result = solution.groupAnagrams(strs=strs)
    print(type(result))

if __name__ == "__main__":
    main()

