#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
"""

class Solution(object):

    def isValidSudoku(self, board: [[str]]) -> bool:
        # 判断行
        i = 0
        while i < 9:
            elements = [e for e in board[i] if e != "."]
            if len(elements) > len(list(set(elements))):
                return False
            i += 1

        # 判断列
        i = 0
        while i < 9:
            elements = [board[j][i] for j in range(9) if board[j][i] != "."]
            if len(elements) > len(list(set(elements))):
                return False
            i += 1

        # 判断小方格
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                elements = []
                for k in range(3):
                    elements.extend([e for e in board[j][i:i+3] if e != "."])
                    j += 1
                if len(elements) > len(list(set(elements))):
                    return False
            i += 3

        return True


def main():
    board = [
      ["5", "3", ".", ".", "7", ".", ".", ".", "."],
      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
      [".", "9", "8", ".", ".", ".", ".", "6", "."],
      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."],
      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
      [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solution = Solution()
    result = solution.isValidSudoku(board=board)
    print(result)

if __name__ == "__main__":
    main()

"""
"""
