#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""

class Solution(object):

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        result = [0] * n
        for i in range(n):
            if i == 0 or i == 1:
                result[i] = 1
            else:
                result[i] = result[i-1] + result[i-2]
        return result[-1] + result[-2]

    def climbStairs2(self, n: int) -> int:
        def back_trace(n):
            if n == 0 or n == 1:
                return 1
            return back_trace(n-1) + back_trace(n-2)
        return back_trace(n)

def main():
    n = 1
    solution = Solution()
    result = solution.climbStairs(n=n)
    print(result)

if __name__ == "__main__":
    main()


