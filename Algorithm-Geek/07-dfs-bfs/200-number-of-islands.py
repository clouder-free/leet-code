# -*- coding: utf-8 -*-

class Solution():

    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    result += 1
                    self.__dfs(grid, i, j)
        return result

    def __dfs(self, grid, r, c):
        m, n = len(grid), len(grid[0])

        grid[r][c] = '0'
        if r-1 >= 0 and grid[r-1][c] == '1':
            self.__dfs(grid, r-1, c)
        if c-1 >= 0 and grid[r][c-1] == '1':
            self.__dfs(grid, r, c-1)
        if c+1 < n and grid[r][c+1] == '1':
            self.__dfs(grid, r, c+1)
        if r+1 < m and grid[r+1][c] == '1':
            self.__dfs(grid, r+1, c)

def main():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    result = Solution().numIslands(grid=grid)
    print(result)


if __name__ == '__main__':
    main()

