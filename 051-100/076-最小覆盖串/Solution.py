#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给你一个字符串S、一个字符串T，请在字符串S里面找出：包含T所有字母的最小子串。
示例：
输入: S = "ADOBECODEBANC", T = "ABC"  输出: "BANC"
说明：
如果S中不存这样的子串，则返回空字符串 ""。
如果S中存在这样的子串，我们保证它是唯一的答案。
"""

class Solution(object):

    def minWindow(self, s: str, t: str) -> str:
        result = ""
        if not s or not t:
            return ""
        left, right = 0, -1
        tdict = {}
        tcount = 0
        for c in t:
            tdict[c] = tdict.get(c, 0) + 1
        while left < len(s):
            # 扩展右边界
            if right+1 < len(s) and tcount < len(t):
                right += 1
                if s[right] in tdict:
                    if tdict[s[right]] > 0:
                        tcount += 1
                    tdict[s[right]] -= 1
            # 收缩左边界
            else:
                if s[left] in tdict:
                    if tdict[s[left]] == 0:
                        tcount -= 1
                    tdict[s[left]] += 1
                left += 1
            # 判断tcount与t的长度
            if tcount == len(t):
                if not result or len(result) > right-left+1:
                    result = s[left:right+1]
        return result

def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    solution = Solution()
    result = solution.minWindow(s=s, t=t)
    print(result)

if __name__ == "__main__":
    main()
