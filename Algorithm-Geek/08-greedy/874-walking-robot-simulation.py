# -*- coding: utf-8 -*-

class Solution(object):

    def robotSim(self, commands: [int], obstacles: [[int]]) -> int:
        directions = {
            'up': {-1: 'right', -2: 'left'},
            'down': {-1: 'left', -2: 'right'},
            'left': {-1: 'up', -2: 'down'},
            'right': {-1: 'down', -2: 'up'}
        }
        x, y = 0, 0
        current = 'up'
        for i in range(len(commands)):
            if commands[i] < 0:
                current = directions[current][commands[i]]
                continue
            # 向上
            if current == 'up':
                ny = y + commands[i]
                for obs in obstacles:
                    if obs[0] == x and y < obs[1] <= ny:
                        y = obs[1] - 1
                        break
                else:
                    y = ny
            # 向下
            elif current == 'down':
                ny = y - commands[i]
                for obs in obstacles:
                    if obs[0] == x and ny <= obs[1] < y:
                        y = obs[1] + 1
                        break
                else:
                    y = ny
            elif current == 'left':
                nx = x - commands[i]
                for obs in obstacles:
                    if obs[1] == y and nx <= obs[0] < x:
                        x = obs[0] + 1
                        break
                else:
                    x = nx
            else:
                nx = x + commands[i]
                for obs in obstacles:
                    if obs[1] == y and x < obs[0] <= nx:
                        x = obs[0] - 1
                        break
                else:
                    x = nx

        return x * x + y * y

def main():
    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    solution = Solution()
    result = solution.robotSim(commands=commands, obstacles=obstacles)
    print(result)

if __name__ == '__main__':
    main()


