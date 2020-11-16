# -*- coding: utf-8 -*-

class Solution(object):

    def isValid(self, s: str) -> bool:
        valid = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in range(len(s)):
            if s[i] in valid:
                stack.append(s[i])
            else:
                if stack and valid[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        return False if stack else True


def main():
    s = ''

