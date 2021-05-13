# -*- coding: utf-8 -*-
"""
回溯
"""

class Solution(object):

    def uniquePathsIII(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.result = 0
        step = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                if grid[i][j] == 2:
                    ex, ey = i, j
                if grid[i][j] != -1:
                    step += 1
        print('sx:', sx, 'sy:', sy)
        print('ex:', ex, 'ey:', ey)
        print('step:', step)
        # 回溯
        def back_trace(x, y, steps):
            steps -= 1
            if x==ex and y==ey:
                if steps == 0:
                    self.result += 1
                    return
            grid[x][y] = -1
            # 四个方向
            for (dx, dy) in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)):
                if 0<=dx<m and 0<=dy<n and grid[dx][dy] != -1:
                    back_trace(dx, dy, steps)
            grid[x][y] = 0
        back_trace(sx, sy, step)
        return self.result


def main():
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    result = Solution().uniquePathsIII(grid=grid)
    print(result)


if __name__ == '__main__':
    main()
