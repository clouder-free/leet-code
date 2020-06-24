#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution(object):

    def spiralOrder(self, matrix: [[int]]) -> [int]:
        results = []
        max_row = len(matrix)
        if max_row == 0:
            return results
        max_col = len(matrix[0])
        # 初始值
        row, col = 0, -1
        # 行 列
        for i in range(max_row // 2 + 1):
            # 左 -> 右
            while col + 1 < max_col and matrix[row][col+1] != "T":
                print('row:{} col:{}'.format(row, col+1))
                results.append(matrix[row][col+1])
                matrix[row][col+1] = "T"
                col += 1
            # 上 -> 下
            while row + 1 < max_row and matrix[row+1][col] != "T":
                print('row:{} col:{}'.format(row+1, col))
                results.append(matrix[row+1][col])
                matrix[row+1][col] = "T"
                row += 1
            # 右 -> 左
            while col - 1 > -1 and matrix[row][col-1] != "T":
                print('row:{} col:{}'.format(row, col-1))
                results.append(matrix[row][col-1])
                matrix[row][col-1] = "T"
                col -= 1
            # 下 -> 上
            while row - 1 > -1 and matrix[row-1][col] != "T":
                print('row:{} col:{}'.format(row-1, col))
                results.append(matrix[row-1][col])
                matrix[row-1][col] = "T"
                row -= 1
        return results


def main():
    matrix = [
             [7],
             [8],
             [9]
            ]
    solution = Solution()
    result = solution.spiralOrder(matrix=matrix)
    print(result)

if __name__ == "__main__":
    main()
