# -*- coding: utf-8 -*-

class Solution(object):

    def solve(self, board: [[str]]) -> None:
        # row, col
        visited = set()
        m, n = len(board), len(board[0])
        dirx = [1, -1, 0, 0]
        diry = [0, 0, 1, -1]

        def _dfs(i, j):
            for k in range(4):
                x = i + dirx[k]
                y = j + diry[k]
                v = '{}_{}'.format(x, y)
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O' and v not in visited:
                    board[x][y] = 'M'
                    visited.add(v)
                    _dfs(x, y)

        # row
        for i in [0, m-1]:
            for j in range(n):
                v = '{}_{}'.format(i, j)
                if board[i][j] == 'O' and v not in visited:
                    visited.add(v)
                    board[i][j] = 'M'
                    _dfs(i, j)
        # col
        for i in range(m):
            for j in [0, n-1]:
                v = '{}_{}'.format(i, j)
                if board[i][j] == 'O' and v not in visited:
                    visited.add(v)
                    board[i][j] = 'M'
                    _dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        print(board)



def main():
    board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['X', 'O', 'X']
    ]
    solution = Solution()
    solution.solve(board=board)


if __name__ == '__main__':
    main()
