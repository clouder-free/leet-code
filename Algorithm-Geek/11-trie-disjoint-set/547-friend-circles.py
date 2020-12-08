# -*- coding: utf-8 -*-

class Solution(object):

    def findCircleNum(self, M: [[int]]) -> int:
        count = 0
        visited = set()
        n = len(M)

        def _dfs(i):
            for j in range(n):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    _dfs(j)

        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                _dfs(i)

        return count

def main():
    M = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    # M = [[1,1,0],
    #      [1,1,0],
    #      [0,0,1]]
    solution = Solution()
    result = solution.findCircleNum(M=M)
    print(result)

if __name__ == '__main__':
    main()






