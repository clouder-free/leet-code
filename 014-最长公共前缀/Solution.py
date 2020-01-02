#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串。
输入: ["flower","flow","flight"] 输出: "fl"
输入: ["dog","racecar","car"] 输出: ""
"""

class Solution(object):

    def longestCommonPrefix(self, strs: [str]) -> str:
        common = ""
        if len(strs) == 0:
            return common
        i = 0
        while True:
            chrs = []
            for str in strs:
                if i < len(str):
                    chrs.append(str[i])
                else:
                    break
            print("index:{} chrs:{}".format(i, chrs))
            if len(chrs) == len(strs) and len(set(chrs)) == 1:
                common += chrs[0]
                i += 1
            else:
                break
        return common

def main():
    strs = ["dog", "racecar", "car"]
    solution = Solution()
    result = solution.longestCommonPrefix(strs=strs)
    print(result)

if __name__ == "__main__":
    main()

"""
["flower","flow","flight"] "fl"
["dog","racecar","car"] ""
"""
