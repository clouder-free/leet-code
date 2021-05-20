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

    # 滑动窗口
    def findAnagrams2(self, s: str, p: str) -> [int]:
        ls, lp = len(s), len(p)
        result = []
        if lp > ls:
            return result
        sw = [0] * 26
        pw = [0] * 26
        for i in range(lp):
            sw[ord(s[i]) - ord('a')] += 1
            pw[ord(p[i]) - ord('a')] += 1
        if sw == pw:
            result.append(0)
        for i in range(lp, ls):
            sw[ord(s[i-lp]) - ord('a')] -= 1
            sw[ord(s[i]) - ord('a')] += 1
            if sw == pw:
                result.append(i-lp+1)
        return result


def main():
    # s = 'abab'
    # p = 'ab'
    s = 'cbaebabacd'
    p = 'abc'
    r = Solution().findAnagrams2(s=s, p=p)
    print(r)


if __name__ == '__main__':
    main()
