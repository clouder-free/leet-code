# -*- coding: utf-8 -*-

class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        # m行 0列
        for i in range(1, m):
            if obstacleGrid[i][0]:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0] if i != 0 else 1
        # 0行 n列
        for i in range(1, n):
            if obstacleGrid[0][i]:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1] if i != 0 else 1
        # m行 n列
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


def main():
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    result = Solution().uniquePathsWithObstacles(obstacleGrid=obstacleGrid)
    print(result)


if __name__ == '__main__':
    main()
