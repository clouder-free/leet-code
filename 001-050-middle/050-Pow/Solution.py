#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
输入: 2.00000, 10  输出: 1024.00000
输入: 2.10000, 3   输出: 9.26100
输入: 2.00000, -2  输出: 0.25000
"""

class Solution(object):

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            n = -n
            x = 1/x
        i = 1
        result = 1.0
        while i <= n:
            result *= x
            i += 1
        if result < -2 ** 31:
            return -2 ** 31
        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return result

    def myPow2(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow2(x, -n)
        elif n % 2:
            return self.myPow2(x*x, n//2) * x
        else:
            return self.myPow2(x*x, n//2)

def main():
    x = 3.0
    n = 3
    solution = Solution()
    result = solution.myPow2(x=x, n=n)
    print(result)

if __name__ == "__main__":
    main()


