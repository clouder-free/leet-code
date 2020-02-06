#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):

    def generateParenthesis(self, n: int) -> [str]:
        results = []
        s = "("
        self.generateQuotes(s=s, n=n, results=results)
        return results

    def generateQuotes(self, s, n, results):
        left = s.count("(")
        right = s.count(")")
        if left >= right:
            if left + right < 2 * n:
                if left < n:
                    self.generateQuotes(s+"(", n, results)
                    self.generateQuotes(s+")", n, results)
                else:
                    self.generateQuotes(s+")", n, results)
            else:
                results.append(s)

def main():
    n = 4
    solution = Solution()
    results = solution.generateParenthesis(n=n)
    print(results)

if __name__ == "__main__":
    main()

"""
输入：([)] 输出：false
"""
