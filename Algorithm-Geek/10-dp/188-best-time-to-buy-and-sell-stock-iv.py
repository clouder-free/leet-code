# -*- coding: utf-8 -*-

class Solution(object):

    def maxProfit(self, k: int, prices: [int]) -> int:
        if not prices:
            return 0
        # dp状态数组
        dp = [[0] * (2*k+1) for _ in range(len(prices))]
        # 初值
        for i in range(1, 2*k, 2):
            dp[0][i] = -prices[0]
        # 循环迭代
        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            for j in range(1, 2*k+1, 2):
                # 买入
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]-prices[i])
                # 卖出
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j]+prices[i])
        return dp[-1][-1]

    def maxProfit2(self, k: int, prices: [int]) -> int:
        # k = min(k, len(prices) // 2)
        buy = [float('-inf')] * (k+1)
        sell = [0] * (k+1)
        for i in range(len(prices)):
            for j in range(1, k+1):
                buy[j] = max(buy[j], sell[j-1]-prices[i])
                sell[j] = max(sell[j], buy[j]+prices[i])
        return sell[-1]


def main():
    prices = [2, 4, 1]
    result = Solution().maxProfit2(k=2, prices=prices)
    print(result)


if __name__ == '__main__':
    main()
