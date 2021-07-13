# -*- coding: utf-8 -*-
"""
找到所有数组中消失的数字
"""

class Solution:

    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        result = []
        n = len(nums)
        numbers = [0] * n
        for num in nums:
            if num <= n:
                numbers[num-1] = 1
        for i in range(n):
            if numbers[i] == 0:
                result.append(i+1)
        return result


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
