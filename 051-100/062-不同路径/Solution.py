#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
一个机器人位于一个 m x n 网格的左上角（起始点在下图中标记为“Start”）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
"""

class Solution(object):

    def uniquePaths(self, m: int, n: int) -> int:
        # m列 n行
        results = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                # i行 j列
                if i == 0 or j == 0:
                    results[i][j] = 1
                else:
                    results[i][j] = results[i-1][j] + results[i][j-1]
        return results[-1][-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        def back_trace(m, n):
            if m == 1 and n == 1:
                return 1
            if m == 1:
                return back_trace(m, n-1)
            if n == 1:
                return back_trace(m-1, n)
            return back_trace(m-1, n) + back_trace(m, n-1)
        return back_trace(m, n)

def main():
    solution = Solution()
    m = 7
    n = 3
    result = solution.uniquePaths(m=m, n=n)
    print(result)

if __name__ == "__main__":
    main()
