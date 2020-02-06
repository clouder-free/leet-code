#! /usr/bin/python
# -*- coding: utf-8 -*

"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
示例 1:
输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:
输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:
一个直接的解决方案是使用O(mn)的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用O(m+n)的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？
"""

class Solution(object):

    def setZeroes(self, matrix: [[int]]) -> None:
        # 所有元素为0的坐标
        results = [[i, j] for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 0]
        # 行置零
        for row in set([result[0] for result in results]):
            matrix[row] = [0] * len(matrix[0])
        # 列置零
        for col in set([result[1] for result in results]):
            for row in range(len(matrix)):
                matrix[row][col] = 0
        print(matrix)

def main():
    solution = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution.setZeroes(matrix=matrix)

if __name__ == "__main__":
    main()



