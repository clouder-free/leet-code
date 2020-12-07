# -*- coding: utf-8 -*-

class Solution(object):

    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1


def main():
    coins = [2]
    amount = 3
    solution = Solution()
    result = solution.coinChange(coins=coins, amount=amount)
    print(result)


if __name__ == '__main__':
    main()

