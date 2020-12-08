# -*- coding: utf-8 -*-

class Solution(object):

    def numIslands(self, grid: [[str]]) -> int:
        count = 0
        visited = set()
        m, n = len(grid), len(grid[0])
        dirx = [1, -1, 0, 0]
        diry = [0, 0, 1, -1]

        def _dfs(i, j):
            for k in range(4):
                x = i + dirx[k]
                y = j + diry[k]
                v = '{}_{}'.format(x, y)
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and v not in visited:
                    visited.add(v)
                    _dfs(x, y)

        for i in range(m):
            for j in range(n):
                v = '{}_{}'.format(i, j)
                if grid[i][j] == '1' and v not in visited:
                    count += 1
                    _dfs(i, j)
        return count


def main():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    solution = Solution()
    result = solution.numIslands(grid=grid)
    print(result)

if __name__ == '__main__':
    main()
