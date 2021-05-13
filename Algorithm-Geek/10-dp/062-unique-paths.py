# -*- coding: utf-8 -*-

class Solution(object):

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        # m行
        for i in range(1, m):
            dp[i][0] = 1
        # n列
        for i in range(1, n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


def main():
    m, n = 3, 7
    result = Solution().uniquePaths(m=m, n=n)
    print(result)


if __name__ == '__main__':
    main()
