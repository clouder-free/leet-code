#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
"""

class Solution(object):

    def divide(self, dividend: int, divisor: int) -> int:
        index = (dividend > 0) == (divisor > 0)
        dividend, divisor, result = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            i = 0
            while dividend >= divisor << (i+1):
                i += 1
            result += 1 << i
            dividend -= divisor << i
        if not index:
            result = -result
        return min(max(-2**31, result), 2**31-1)

def main():
    dividend = 2147483647
    divisor = 2
    solution = Solution()
    result = solution.divide(dividend=dividend, divisor=divisor)
    print(result)

if __name__ == "__main__":
    main()

"""
输入: dividend = 10, divisor = 3 输出: 3
输入: dividend = 7, divisor = -3 输出: -2
"""
