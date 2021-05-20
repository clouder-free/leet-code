# -*- coding: utf-8 -*-

class Solution(object):

    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        # 层序遍历
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        queue = [(0, 0)]
        result = 1
        while queue:
            temp = []
            for i in range(len(queue)):
                x, y = queue[i]
                if x == m-1 and y == n-1:
                    return result
                # 8个方向
                for (dx, dy) in ((x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)):
                    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 0:
                        grid[dx][dy] = 1
                        temp.append((dx, dy))
            queue = temp[:]
            result += 1
        return -1

        # if not grid or grid[0][0] == 1:
        #     return -1
        # n = len(grid)
        # result = n * n
        # def _bfs(x, y, step):
        #     nonlocal result
        #     step += 1
        #     if x == n-1 and y == n-1:
        #         if step < result:
        #             result = step
        #         return
        #     grid[x][y] = 1
        #     for (dx, dy) in ((x-1, y-1), (x-1, y), (x-1, y+1),
        #                      (x, y-1), (x, y+1),
        #                      (x+1, y-1), (x+1, y), (x+1, y+1)):
        #         # print('for-- dx:', dx, 'dy:', dy)
        #         if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] == 0:
        #             _bfs(dx, dy, step)
        #     grid[x][y] = 0
        # _bfs(0, 0, 0)
        # return result if result != n*n else -1


def main():
    # grid = [[0, 1], [1, 0]]
    # grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    # grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    grid = [[0,0,1,1,0,0],[0,0,0,0,1,1],[1,0,1,1,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,1,0,0,0]]
    result = Solution().shortestPathBinaryMatrix(grid=grid)
    print(result)


if __name__ == '__main__':
    main()
