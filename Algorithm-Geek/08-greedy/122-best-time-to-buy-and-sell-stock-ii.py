# -*- coding: utf-8 -*-

class Solution(object):

    def maxProfit(self, prices: [int]) -> int:
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]
        return total


def main():
    prices = []
    solution = Solution()
    result = solution.maxProfit(prices=prices)
    print(result)

if __name__ == '__main__':
    main()

