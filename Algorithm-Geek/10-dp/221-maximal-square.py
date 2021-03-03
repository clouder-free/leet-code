# -*- coding: utf-8 -*-

class Solution(object):

    def maximalSquare(self, matrix: [[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        side = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1
                side = max(side, dp[i][j])
        return side * side


def main():
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    result = Solution().maximalSquare(matrix=matrix)
    print(result)


if __name__ == '__main__':
    main()
