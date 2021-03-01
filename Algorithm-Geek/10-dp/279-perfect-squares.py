# -*- coding: utf-8 -*-


class Solution(object):

    def numSquares(self, n: int) -> int:
        """动态规划"""
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = i
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[-1]


def main():
    n = 12
    result = Solution().numSquares(n=n)
    print(result)


if __name__ == '__main__':
    main()
