# -*- coding: utf-8 -*-
"""
搜索二维矩阵II
"""

class Solution:

    def searchMatrix(self, matrix: [[int]], target) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 左下角
        i, j = m-1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
