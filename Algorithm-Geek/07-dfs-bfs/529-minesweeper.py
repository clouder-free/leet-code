# -*- coding: utf-8 -*-
"""
"""

class Solution(object):

    def updateBoard(self, board: [[str]], click: [int]) -> [[str]]:
        m, n = len(board), len(board[0])
        r, c = click
        # 炸弹 结束退出
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        # 相邻炸弹 则修改数字退出
        count = self.__bombCount(board, click)
        if count > 0:
            board[r][c] = str(count)
            return board
        # 相邻啥都没有 修改成B 然后条件扩散
        board[r][c] = 'B'
        # 递归挖四周
        # 上一行
        if r-1 >= 0:
            if c-1 >= 0 and board[r-1][c-1] == 'E':
                self.updateBoard(board, [r-1, c-1])
            if board[r-1][c] == 'E':
                self.updateBoard(board, [r-1, c])
            if c+1 < n and board[r-1][c+1] == 'E':
                self.updateBoard(board, [r-1, c+1])
        # 同一行
        if c-1 >= 0 and board[r][c-1] == 'E':
            self.updateBoard(board, [r, c-1])
        if c+1 < n and board[r][c+1] == 'E':
            self.updateBoard(board, [r, c+1])
        # 下一行
        if r+1 < m:
            if c-1 >= 0 and board[r+1][c-1] == 'E':
                self.updateBoard(board, [r+1, c-1])
            if board[r+1][c] == 'E':
                self.updateBoard(board, [r+1, c])
            if c+1 < n and board[r+1][c+1] == 'E':
                self.updateBoard(board, [r+1, c+1])
        return board

    def __bombCount(self, board: [[str]], click: [int]) -> int:
        m, n = len(board), len(board[0])
        r, c = click
        count = 0
        # 上一行
        if r-1 >= 0:
            if c-1 >= 0 and board[r-1][c-1] == 'M':
                count += 1
            if board[r-1][c] == 'M':
                count += 1
            if c+1 < n and board[r-1][c+1] == 'M':
                count += 1
        # 同一行
        if c-1 >= 0 and board[r][c-1] == 'M':
            count += 1
        if c+1 < n and board[r][c+1] == 'M':
            count += 1
        # 下一行
        if r+1 < m:
            if c-1 >= 0 and board[r+1][c-1] == 'M':
                count += 1
            if board[r+1][c] == 'M':
                count += 1
            if c+1 < n and board[r+1][c+1] == 'M':
                count += 1
        return count

    def updateBoard2(self, board: [[str]], click: [int]) -> [[str]]:
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        self._dfs(board, x, y)
        return board

    def _dfs(self, board, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        m, n = len(board), len(board[0])
        for direction in directions:
            dx, dy = x+direction[0], y+direction[1]
            if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == 'M':
                count += 1
        if count > 0:
            board[x][y] = str(count)
            return
        board[x][y] = 'B'
        for direction in directions:
            dx, dy = x+direction[0], y+direction[1]
            if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == 'E':
                self._dfs(board, dx, dy)


def main():
    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    # board = [["E", "E", "E", "E", "E", "E", "E", "E"],
    #          ["E", "E", "E", "E", "E", "E", "E", "M"],
    #          ["E", "E", "M", "E", "E", "E", "E", "E"],
    #          ["M", "E", "E", "E", "E", "E", "E", "E"],
    #          ["E", "E", "E", "E", "E", "E", "E", "E"],
    #          ["E", "E", "E", "E", "E", "E", "E", "E"],
    #          ["E", "E", "E", "E", "E", "E", "E", "E"],
    #          ["E", "E", "M", "M", "E", "E", "E", "E"]]
    # board = [["M","M","M","M","M","M"],
    #          ["M","M","M","E","M","M"],
    #          ["M","M","M","M","M","M"]]
    click = [1, 3]
    result = Solution().updateBoard(board, click)
    print(result)
    print(Solution().updateBoard2(board, click))


if __name__ == '__main__':
    main()
