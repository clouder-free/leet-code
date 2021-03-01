# -*- coding: utf-8 -*-

class Solution(object):

    def isMatch(self, s: str, p: str) -> bool:
        # 判空
        if p == '':
            return s == ''
        # 讨论
        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            # 首字符匹配
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s, p[2:])
        else:
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False




def main():
    s = ''
    p = ''

    print("Hello World!")


if __name__ == '__main__':
    main()
