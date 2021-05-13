# -*- coding: utf-8 -*-

class Solution(object):

    def maxProfit(self, prices: [int]) -> int:
        if not prices:
            return 0
        # dp[i][0] 持有股票 累计收益
        # dp[i][1] 不持有股票 冷冻期内 累计收益
        # dp[i][2] 不持有股票 不在冷冻期 累计收益
        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[-1][1], dp[-1][2])

    def maxProfit2(self, prices: [int]) -> int:
        buy, pre, sell = float('-inf'), 0, 0
        for i in range(len(prices)):
            buy = max(buy, pre-prices[i])
            pre, sell = sell, max(sell, buy+prices[i])
        return sell


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
