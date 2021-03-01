# -*- coding: utf-8 -*-

class Solution(object):

    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        i, j = 1, 2
        result = 0
        for m in range(3, n+1):
            result = i + j
            i, j = j, result
        return result

    def climbStairs2(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        return dp[-1]


def main():
    n = 4
    solution = Solution()
    result = solution.climbStairs2(n=n)
    print(result)


if __name__ == '__main__':
    main()

