# -*- coding: utf-8 -*-

class Solution(object):

    def isAnagram(self, s: str, t: str) -> bool:
        # 判断长度
        if len(s) != len(t):
            return False
        # 对s,t进行排序
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        for i in range(len(s)):
            if ls[i] != lt[i]:
                return False
        return True


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
