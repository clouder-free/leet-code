#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""

class Solution(object):

    def isValid(self, s: str) -> bool:
        quote = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        temp = ""
        for i in range(len(s)):
            if s[i] in "([{":
                temp += s[i]
            else:
                if len(temp) > 0 and quote.get(temp[-1], "") == s[i]:
                    temp = temp[:-1]
                else:
                    return False
        if len(temp) > 0:
            return False
        return True

def main():
    s = "{[]}"
    solution = Solution()
    result = solution.isValid(s=s)
    print(result)

if __name__ == "__main__":
    main()

"""
输入：([)] 输出：false
"""
