# -*- coding: utf-8 -*-

class Solution(object):

    def minCostClimbingStairs(self, cost: [int]) -> int:
        dp = [0, 0]
        for i in range(2, len(cost)+1):
            dp.append(min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2]))
        return dp[-1]

    def minCostClimbingStairs2(self, cost: [int]) -> int:
        x, y = 0, 0
        for i in range(2, len(cost)+1):
            x, y = y, min(cost[i-1]+y, cost[i-2]+x)
        return y


def main():
    # cost = [10, 15, 20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    solution = Solution()
    result = solution.minCostClimbingStairs(cost=cost)
    print(result)


if __name__ == '__main__':
    main()



