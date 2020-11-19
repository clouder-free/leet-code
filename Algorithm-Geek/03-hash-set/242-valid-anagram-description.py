# -*- coding: utf-8 -*-

class Solution(object):

    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        for i in range(len(s)):
            if s[i] not in sd:
                sd[s[i]] = 0
            sd[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in sd:
                return False
            sd[t[i]] -= 1
            if sd[t[i]] < 0:
                return False
        for k, v in sd.items():
            if v != 0:
                return False
        return True


def main():
    # s = 'anagram'
    # t = 'nagaram'
    # s = 'rat'
    # t = 'car'
    s = 'aa'
    t = 'a'
    solution = Solution()
    result = solution.isAnagram(s=s, t=t)
    print(result)

if __name__ == '__main__':
    main()


