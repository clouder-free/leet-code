# -*- coding: utf-8 -*-

class Solution(object):

    def maxProfit(self, prices: [int], fee: int) -> int:
        if not prices:
            return 0
        # dp[i][0] 第i天 手里没有股票
        # dp[i][1] 第i天 手里有股票
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[-1][0]


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
