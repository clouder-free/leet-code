# -*- coding: utf-8 -*-

class Solution(object):

    def minPathSum(self, grid: [[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 左上角
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                # 0行 j列
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                # i行 0列
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                # i行 j列
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]


def main():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = Solution().minPathSum(grid=grid)
    print(result)


if __name__ == '__main__':
    main()
