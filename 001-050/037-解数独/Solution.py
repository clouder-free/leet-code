#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
编写一个程序，通过已填充的空格来解决数独问题。
一个数独的解法需遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
"""

class Solution(object):

    # 回溯法求解
    def solveSudoku(self, board: [[str]]) -> None:
        # 全部数据 行/列/宫格
        rows = [set(range(1, 10)) for _ in range(9)]
        cols = [set(range(1, 10)) for _ in range(9)]
        cubes = [set(range(1, 10)) for _ in range(9)]
        dots = []
        # 行i 列j
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    dots.append((i, j))
                else:
                    rows[i].remove(int(board[i][j]))
                    cols[j].remove(int(board[i][j]))
                    cubes[i//3*3+j//3].remove(int(board[i][j]))
        def backtrace():
            if not dots:
                return True
            i, j = dots.pop()
            values = rows[i] & cols[j] & cubes[i//3*3+j//3]
            for val in values:
                rows[i].remove(val)
                cols[j].remove(val)
                cubes[i//3*3+j//3].remove(val)
                board[i][j] = str(val)
                if backtrace():
                    return True
                # 回溯
                rows[i].add(val)
                cols[j].add(val)
                cubes[i // 3 * 3 + j // 3].add(val)
            else:
                # 回溯
                dots.append((i, j))
                return False
        backtrace()

    def solveSudoku2(self, board: [[str]]) -> None:
        dots = []
        # 行i 列j
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    dots.append((i, j))
        # 循环求值
        while dots:
            for dot in dots:
                i, j = dot
                # 第i行所有的数
                rownums = [n for n in board[i] if n != "."]
                # 第j列所有的数
                colnums = [board[n][j] for n in range(9) if board[n][j] != "."]
                # i, j 位于宫格所有的数
                cubex = i // 3 * 3
                cubey = j // 3 * 3
                cubenums = [board[m][n] for m in range(cubex, cubex+3) for n in range(cubey, cubey+3) if board[m][n] != "."]
                rownums.extend(colnums)
                rownums.extend(cubenums)
                diff = set([i for i in range(1, 10)]) - set(rownums)
                # 当前格子只有一个值 数独可解
                if len(diff) == 1:
                    board[i][j] = list(diff)[0]
                    # 移除当前值
                    dots.remove(dot)

def main():
    board = [
        [5, 3, '.', '.', 7, '.', '.', '.', '.'],
        [6, '.', '.', 1, 9, 5, '.', '.', '.'],
        ['.', 9, 8, '.', '.', '.', '.', 6, '.'],
        [8, '.', '.', '.', 6, '.', '.', '.', 3],
        [4, '.', '.', 8, '.', 3, '.', '.', 1],
        [7, '.', '.', '.', 2, '.', '.', '.', 6],
        ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
        ['.', '.', '.', 4, 1, 9, '.', '.', 5],
        ['.', '.', '.', '.', 8, '.', '.', 7, 9],
    ]
    solution = Solution()
    solution.solveSudoku(board=board)

if __name__ == "__main__":
    main()

