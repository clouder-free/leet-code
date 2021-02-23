# -*- coding: utf-8 -*-

class Solution(object):

    def groupAnagrams(self, strs: [str]) -> [[str]]:
        sd = {}
        for s in strs:
            ls = list(s)
            ls.sort()
            key = ''.join(ls)
            if key not in sd:
                sd[key] = []
            sd[key].append(s)
        return list(sd.values())


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs=strs)
    print(result)


if __name__ == '__main__':
    main()
