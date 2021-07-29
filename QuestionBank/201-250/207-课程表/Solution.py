# -*- coding: utf-8 -*-
"""
课程表
"""

class Solution:

    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        # bfs 入度/邻接表
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = []
        # 初始化数据
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        print('indegrees:', indegrees)
        print('adjacency:', adjacency)
        # 入度为0的节点入队
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)
        print('queue:', queue)
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses

def main():
    numCourses = 2
    prerequisites = [[1, 0]]
    print(Solution().canFinish(numCourses, prerequisites))


if __name__ == '__main__':
    main()
