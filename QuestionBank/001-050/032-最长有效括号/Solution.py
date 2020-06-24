#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
输入: "(()" 输出: 2
解释: 最长有效括号子串为 "()"
输入: ")()())" 输出: 4
解释: 最长有效括号子串为 "()()"
"""

class Solution(object):

    def longestValidParentheses(self, s: str) -> int:
        result = 0
        start, stack = 0, []
        for i in range(len(s)):
            # 左括号入栈
            if s[i] == "(":
                stack.append(i)
            # 右括号出栈 栈不为空
            elif stack:
                stack.pop()
                # 栈不为空
                if stack:
                    result = i-stack[-1] if i-stack[-1] > result else result
                # 栈为空
                else:
                    result = i-start+1 if i-start+1 > result else result
            # 右括号 栈为空
            else:
                start = i+1
        # print("start:", start, "stack:", stack)
        return result

def main():
    s = "(()"
    solution = Solution()
    result = solution.longestValidParentheses(s=s)
    print(result)

if __name__ == "__main__":
    main()
