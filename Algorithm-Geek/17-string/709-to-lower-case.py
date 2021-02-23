# -*- coding: utf-8 -*-

class Solution(object):

    def toLowerCase(self, str: str) -> str:
        if not str.islower():
            str = str.lower()
        return str


def main():
    s = 'Hello'
    res = Solution().toLowerCase(str=s)
    print(res)


if __name__ == '__main__':
    main()
