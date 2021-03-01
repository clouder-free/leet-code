# -*- coding: utf-8 -*-

class Solution(object):

    def maxProfit(self, prices: [int]) -> int:
        if not prices:
            return 0
        mp = prices[0]
        result = 0
        for i in range(len(prices)):
            if mp > prices[i]:
                mp = prices[i]
            if prices[i]-mp > result:
                result = prices[i]-mp
        return result


def main():
    prices = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(prices=prices)
    print(result)


if __name__ == '__main__':
    main()
