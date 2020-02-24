#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二维平面，平面上有n个点，求最多有多少个点在同一条直线上。
输入: [[1,1],[2,2],[3,3]] 输出: 3
输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] 输出: 4
"""

class Solution(object):

    def maxPoints(self, points: [[int]]) -> int:
        from decimal import Decimal
        slopes = {}
        result = 0
        for i in range(len(points)):
            slopes.clear()
            duplicate = 1
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    duplicate += 1
                    continue

                if x1 == x2:
                    slopes["X"] = slopes.get("X", 0) + 1
                else:
                    slop = Decimal(y2 - y1) / Decimal(x2 - x1)
                    slopes[slop] = slopes.get(slop, 0) + 1

            if result < duplicate:
                result = duplicate

            for _, v in slopes.items():
                if v + duplicate > result:
                    result = v + duplicate

        return result

def main():
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    solution = Solution()
    result = solution.maxPoints(points=points)
    print(result)

if __name__ == "__main__":
    main()




