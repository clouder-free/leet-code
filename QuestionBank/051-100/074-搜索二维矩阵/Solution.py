#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。
该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
"""

class Solution(object):

    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0:
            return False
        for row in matrix:
            if not row:
                return False
            if target <= row[-1]:
                for col in row:
                    if target < col:
                        return False
                    elif target == col:
                        return True
        else:
            return False

def main():
    matrix = [[1, 3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 13
    solution = Solution()
    result = solution.searchMatrix(matrix=matrix, target=target)
    print(result)

if __name__ == "__main__":
    main()

