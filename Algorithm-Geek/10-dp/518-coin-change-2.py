# -*- coding: utf-8 -*-

class Solution(object):

    def change(self, amount: int, coins: [int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] += dp[x-coin]
        return dp[-1]


def main():
    amount = 5
    coins = [1, 2, 5]
    result = Solution().change(amount=amount, coins=coins)
    print(result)


if __name__ == '__main__':
    main()
