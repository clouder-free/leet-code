# -*- coding: utf-8 -*-

class Solution(object):

    def robotSim(self, commands: [int], obstacles: [[int]]) -> int:
        result = 0
        direction_x = (0, 1, 0, -1)
        direction_y = (1, 0, -1, 0)
        _obstacle = set()
        for obs in obstacles:
            _obstacle.add(str(obs[0]) + ',' + str(obs[1]))
        x, y, direction = 0, 0, 0
        for command in commands:
            if command == -2:
                direction = (direction + 3) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                for i in range(1, command+1):
                    nx = x + direction_x[direction]
                    ny = y + direction_y[direction]
                    loc = str(nx) + ',' + str(ny)
                    if loc in _obstacle:
                        break
                    x, y = nx, ny
                    result = max(x*x+y*y, result)
        return result


def main():
    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    solution = Solution()
    result = solution.robotSim(commands=commands, obstacles=obstacles)
    print(result)

if __name__ == '__main__':
    main()


