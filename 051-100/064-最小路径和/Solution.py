#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个包含非负整数的m*n网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

class Solution(object):

    def minPathSum(self, grid: [[int]]) -> int:
        # i行 j列
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0:
                    if j == 0:
                        continue
                    else:
                        grid[i][j] += grid[i][j-1]
                else:
                    if j == 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        grid[i][j] += min([grid[i-1][j], grid[i][j-1]])
        print(grid)
        return grid[-1][-1]

def main():
    solution = Solution()
    grid = [
      [1, 3, 1],
      [1, 5, 1],
      [4, 2, 1]
    ]
    result = solution.minPathSum(grid=grid)
    print(result)

if __name__ == "__main__":
    main()
