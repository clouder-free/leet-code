#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
输入: 4 输出: 2
输入: 8 输出: 2 说明: 8 的平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
"""

class Solution(object):

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x // 2
        while left < right:
            # 取右中位数
            mid = (left + right + 1) // 2
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid
        return left

def main():
    x = 0
    solution = Solution()
    result = solution.mySqrt(x=x)
    print(result)

if __name__ == "__main__":
    main()
