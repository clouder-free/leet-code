# -*- coding: utf-8 -*-

class Solution(object):

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        for c in s:
            sd[c] = sd.get(c, 0) + 1
        for c in t:
            if c not in sd:
                return False
            sd[c] -= 1
            if sd[c] == 0:
                del sd[c]
        return not sd


def main():
    # s = 'anagram'
    # t = 'nagaram'
    s = 'rat'
    t = 'car'
    res = Solution().isAnagram(s=s, t=t)
    print(res)


if __name__ == '__main__':
    main()
