# -*- coding: utf-8 -*-

class Solution(object):

    def isPalindrome(self, s: str) -> bool:
        alph = [c.lower() for c in s if c.isalpha() or c.isnumeric()]
        return ''.join(alph) == ''.join(alph[::-1])


def main():
    s = "A man, a plan, a canal: Panama"
    res = Solution().isPalindrome(s=s)
    print(res)


if __name__ == '__main__':
    main()
