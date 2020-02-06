#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""

class Solution(object):

    def letterCombinations(self, digits: str) -> [str]:
        inits = {
            2: "abc", 3: "def", 4: "ghi", 5: "jkl",
            6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }
        if digits:
            return self.spliceCombinations(s=[inits[int(digit)] for digit in digits])
        else:
            return []
        # strs = [inits[int(digit)] for digit in digits]
        # print(strs)

    def spliceCombinations(self, s):
        if len(s) == 1:
            return [i for i in s[0]]
        if len(s) == 2:
            return [i + j for i in s[0] for j in s[1]]
        return [i + j for i in s[0] for j in self.spliceCombinations(s[1:])]

def main():
    # s = ["123", "456", "78"]
    digits = "2"
    solution = Solution()
    result = solution.letterCombinations(digits=digits)
    print(result)
    print(len(result))
    # results = spliceCombinations(s)
    # print(results)


if __name__ == "__main__":
    main()

