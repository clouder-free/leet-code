# -*- coding: utf-8 -*-

class Solution:

    def groupAnagrams(self, strs: [str]) -> [[str]]:
        sd = {}
        for s in strs:
            t = list(s)
            t.sort()
            tpl = ''.join(t)
            if tpl not in sd:
                sd[tpl] = []
            sd[tpl].append(s)
        return list(sd.values())

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    result = solution.groupAnagrams(strs=strs)
    print(result)

if __name__ == '__main__':
    main()



