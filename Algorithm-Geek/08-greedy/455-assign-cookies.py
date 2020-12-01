# -*- coding: utf-8 -*-

class Solution(object):

    def findContentChildren(self, g: [int], s: [int]) -> int:
        g.sort()
        s.sort()
        count = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                count += 1
            j += 1
        return count

def main():
    g = [1, 2]
    s = [1, 2, 3]
    solution = Solution()
    result = solution.findContentChildren(g=g, s=s)
    print(result)

if __name__ == '__main__':
    main()

