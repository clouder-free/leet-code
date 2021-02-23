# -*- coding: utf-8 -*-

class Solution(object):

    def myAtoi(self, s: str) -> int:
        if not s or not s.strip():
            return 0
        start = s.strip()[0]
        if start == '+' or start == '-' or '0' <= start <= '9':
            val = start
            for c in s.strip()[1:]:
                if '0' <= c <= '9':
                    val += c
                else:
                    break
            if val == '-' or val == '+':
                return 0
            elif int(val) < -2 ** 31:
                return -2 ** 31
            elif int(val) > 2 ** 31:
                return 2 ** 31
            else:
                return int(val)
        else:
            return 0


def main():
    # s = '42'
    # s = '    -42'
    # s = '4193 with words'
    # s = 'words and 987'
    # s = '-91283472332'
    s = '-+0000+-023'
    r = Solution().myAtoi(s=s)
    print(r)


if __name__ == '__main__':
    main()
