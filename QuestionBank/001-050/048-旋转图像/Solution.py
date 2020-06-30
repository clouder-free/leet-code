#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

class Solution(object):

    def rotate(self, matrix: [[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()
    
    # 顺时针旋转90
    def rotateClockwise(self, matrix: [[int]]) -> None:
        # 转置 正对角线
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 列互换
        for line in matrix:
            line.reverse()
        
        print(matrix)

    # 逆时针旋转90
    def rotateCounterclockwise(self, matrix: [[int]]) -> None:
        # 行转列
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 逆序 矩阵整体逆序
        matrix[::] = matrix[::-1]
        
        print(matrix)

def main():
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    print(matrix)
    solution = Solution()
    # solution.rotate(matrix=matrix)
    # solution.rotateClockwise(matrix=matrix)
    solution.rotateCounterclockwise(matrix=matrix)

if __name__ == "__main__":
    # main()
    words = ["eat", "tea"]
    for word in words:
        k = list(word)
        k.sort()
        kw = "".join(k)
        print(kw)
    
    
"""
两种解法：
1：先对原矩阵进行转置 再对每行进行逆序
2：按照旋转的策略 从外到内 依次进行赋值操作
"""
