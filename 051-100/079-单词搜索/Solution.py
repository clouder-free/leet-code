#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。
示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
"""

class Solution(object):

    # 深度优先遍历
    def exist(self, board: [[str]], word: str) -> bool:
        def dfs(board, visited, word, x, y):
            # board原数组 visited是否访问过 word拼接字符 x, y当前坐标
            # 行列
            m, n = len(board), len(board[0])
            # 找到数据
            if not word:
                return True
            # 坐标越界/已访问过/当前值!=word[0]
            if x < 0 or x >= m or y < 0 or y >= n or\
               visited[x][y] or \
               board[x][y] != word[0]:
                return False
            visited[x][y] = True
            # 四周扩散
            if dfs(board, visited, word[1:], x-1, y) or \
                dfs(board, visited, word[1:], x+1, y) or \
                dfs(board, visited, word[1:], x, y-1) or \
                dfs(board, visited, word[1:], x, y+1):
                return True
            else:
                visited[x][y] = False
                return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                visited = [[False] * n for i in range(m)]
                if dfs(board=board, visited=visited, word=word, x=i, y=j):
                    return True
        return False

def main():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'E', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCESEEEFS"
    solution = Solution()
    result = solution.exist(board=board, word=word)
    print(result)

if __name__ == "__main__":
    main()


