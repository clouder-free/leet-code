# -*- coding: utf-8 -*-

class Solution(object):

    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
