#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
n皇后问题研究的是如何将n个皇后放置在n×n的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回所有不同的n皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，
该方案中 'Q' 和 '.' 分别代表了皇后和空位。
"""

class Solution(object):

    def solveNQueens(self, n: int) -> [[str]]:
        results = []
        if n == 1:
            return [["Q"]]
        if n < 4:
            return results
        queens = ["." * n for _ in range(n)]
        # 当前放置位置是否有效
        def valid(row, col):
            # 判断列是否有效
            for i in range(row):
                # 同一列是否有Q
                if queens[i][col] == "Q":
                    return False
                j = queens[i].find("Q")
                # 是否处于正反对角线
                if abs(row-i) == abs(col-j):
                    return False
            return True
        def back_trace(i):
            # 放置第i个queen
            if i == n:
                results.append(queens[:])
                return
            # 未全部放完
            for j in range(n):
                q = queens[i]
                queens[i] = q[:j] + "Q" + q[j+1:]
                # 判断当前位置是否有效
                if valid(i, j):
                    back_trace(i+1)
                # 回溯
                queens[i] = "." * n

        back_trace(0)
        return results

def main():
    n = 5
    solution = Solution()
    results = solution.solveNQueens(n=n)
    print(results)

if __name__ == "__main__":
    main()
