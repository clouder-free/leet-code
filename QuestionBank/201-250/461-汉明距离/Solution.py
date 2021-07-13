# -*- coding: utf-8 -*-
"""
汉明距离
"""

class Solution:

    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        while x or y:
            bx = x % 2
            by = y % 2
            if bx != by:
                result += 1
            x = x // 2
            y = y // 2
        return result

def main():
    x, y = 4, 1
    # x, y = 3, 1
    print(Solution().hammingDistance(x, y))


if __name__ == '__main__':
    main()
