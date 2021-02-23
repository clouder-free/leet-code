# -*- coding: utf-8 -*-

class Solution(object):

    def findAnagrams(self, s: str, p: str) -> [int]:
        res = []
        ls, lp = len(s), len(p)
        pk = list(p)
        pk.sort()
        pk = ''.join(pk)
        for i in range(ls-lp+1):
            sk = list(s[i:i+lp])
            sk.sort()
            sk = ''.join(sk)
            if pk == sk:
                res.append(i)
        return res


def main():
    # s = 'abab'
    # p = 'ab'
    s = 'cbaebabacd'
    p = 'abc'
    r = Solution().findAnagrams(s=s, p=p)
    print(r)


if __name__ == '__main__':
    main()
