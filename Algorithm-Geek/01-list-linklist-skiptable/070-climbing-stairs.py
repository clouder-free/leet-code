# -*- coding: utf-8 -*-

class Solution(object):

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        i, j = 1, 2
        k = 2
        while k < n:
            i, j = j, i+j
            k += 1
        return j

    """动态规划"""
    def climbStairs2(self, n: int) -> int:
        dp = [1, 1]
        if n == 1:
            return dp[-1]
        for i in range(2, n+1):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]

def main():
    n = 5
    solution = Solution()
    result = solution.climbStairs2(n=n)
    print(result)

if __name__ == '__main__':
    main()

