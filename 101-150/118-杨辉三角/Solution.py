#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个非负整数 numRows，生成杨辉三角的前numRows行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):

    def generate(self, numRows: int) -> [[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for i in range(3, numRows+1):
            temp = []
            j = 0
            while j < len(result[-1]) - 1:
                temp.append(result[-1][j] + result[-1][j+1])
                j += 1
            result += [[1] + temp + [1]]
        return result

def main():
    numRows = 5
    solution = Solution()
    result = solution.generate(numRows=numRows)
    print(result)

if __name__ == "__main__":
    main()
