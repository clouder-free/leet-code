#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""

class Solution(object):

    def isPalindrome(self, x: int) -> bool:
        from functools import reduce
        if x < 0:
            return False
        y = x
        reverseNumbers = []
        reverseNumbers.append(y % 10)
        y = y // 10
        while y != 0:
            reverseNumbers.append(y % 10)
            y = y // 10
        result = reduce(lambda i, j: 10*i + j, reverseNumbers)
        return result == x

    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        i = 0
        j = x
        while j != 0:
            k = j % 10
            i = 10 * i + k
            j = j // 10
        return i == x

def main():
    x = 450
    solution = Solution()
    result = solution.isPalindrome2(x=x)
    print(result)

if __name__ == "__main__":
    main()
