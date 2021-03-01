# -*- coding: utf-8 -*-

"""至多交易两次"""
class Solution(object):

    def maxProfit(self, prices: [int]) -> int:
        if not prices:
            return 0
        """5种状态 0: 无操作 1: 第1次买入 2: 第1次卖出 3: 第2次买入 4: 第2次卖出"""
        dp = [[0] * (2*2+1) for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, len(prices)):
            # 无操作
            dp[i][0] = dp[i-1][0]
            # 第1次买入
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
            # 第1次卖出
            dp[i][2] = max(dp[i-1][1]+prices[i], dp[i-1][2])
            # 第2次买入
            dp[i][3] = max(dp[i-1][3], dp[i-1][2]-prices[i])
            # 第2次卖出
            dp[i][4] = max(dp[i-1][4], dp[i-1][3]+prices[i])
        return dp[-1][-1]


def main():
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    result = Solution().maxProfit(prices=prices)
    print(result)


if __name__ == '__main__':
    main()
