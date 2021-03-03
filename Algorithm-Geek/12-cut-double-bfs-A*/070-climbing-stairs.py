# -*- coding: utf-8 -*-

class Solution(object):

    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


def main():
    n = 3
    result = Solution().climbStairs(n=n)
    print(result)


if __name__ == '__main__':
    main()
