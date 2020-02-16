#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
输入: "A man, a plan, a canal: Panama" 输出: true
输入: "race a car" 输出: false
"""

class Solution(object):

    def isPalindrome(self, s: str) -> bool:
        positives = [c.lower() for c in s if c.isalnum()]
        # print("positives:", positives)
        p = "".join(positives)
        # print("p:", p)
        positives.reverse()
        # print("reverse:", positives)
        q = "".join(positives)
        # print("q:", q)
        return p == q

    def isPalindrome2(self, s: str) -> bool:
        if not s or not s.strip():
            return True
        i, j = 0, len(s)-1
        while i <= j:
            while i <= j and not s[i].isalpha() and not s[i].isnumeric():
                i += 1
            while i <= j and not s[j].isalpha() and not s[j].isnumeric():
                j -= 1
            if i <= j:
                if s[i].isalpha() and s[j].isalpha() or (s[i].isnumeric() and s[j].isnumeric()):
                    if s[i].lower() == s[j].lower():
                        i += 1
                        j -= 1
                    else:
                        return False
                else:
                    return False
        return True


def main():
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    solution = Solution()
    result = solution.isPalindrome(s=s)
    print(result)

if __name__ == "__main__":
    main()