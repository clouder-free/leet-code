#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution(object):

    def generateMatrix(self, n: int) -> [[int]]:
        # 矩阵初始化
        result = [[-1] * n for i in range(n)]
        row, col = 0, -1
        i = 1
        while i <= n * n:
            # 左->右
            while col + 1 < n and result[row][col+1] == -1 and i <= n * n:
                result[row][col+1] = i
                col += 1
                i += 1
            # 上->下
            while row + 1 < n and result[row+1][col] == -1 and i <= n * n:
                result[row+1][col] = i
                row += 1
                i += 1
            # 右->左
            while col - 1 > -1 and result[row][col-1] == -1 and i <= n * n:
                result[row][col-1] = i
                col -= 1
                i += 1
            # 下->上
            while row - 1 > -1 and result[row-1][col] == -1 and i <= n * n:
                result[row-1][col] = i
                i += 1
                row -= 1
        return result


def main():
    n = 4
    solution = Solution()
    result = solution.generateMatrix(n=n)
    print(result)

if __name__ == "__main__":
    main()
