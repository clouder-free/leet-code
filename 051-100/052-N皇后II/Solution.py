#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回 n 皇后不同的解决方案的数量。
输入: 4  输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution(object):

    # 非递归方式实现
    def totalNQueens(self, n: int) -> int:
        results = []
        if n == 1:
            return 1
        if n < 4:
            return 0
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
                if abs(row - i) == abs(col - j):
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
                queens[i] = q[:j] + "Q" + q[j + 1:]
                # 判断当前位置是否有效
                if valid(i, j):
                    back_trace(i + 1)
                # 回溯
                queens[i] = "." * n

        back_trace(0)
        return len(results)

def main():
    n = 5
    solution = Solution()
    result = solution.totalNQueens(n=n)
    print(result)

if __name__ == "__main__":
    main()

