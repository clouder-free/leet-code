# -*- coding: utf-8 -*-

class Solution(object):

    def findWords(self, board: [[str]], words: [str]) -> [str]:

        # 构造Trie
        tries = {}
        for word in words:
            ct = tries
            for w in word:
                if w not in ct:
                    ct[w] = {}
                ct = ct[w]

        result = []
        m, n = len(board), len(board[0])
        # BFS
        def _bfs(i, j, visited, temp, temp_tries):
            if not temp_tries:
                result.append(''.join(temp))
                return
            v = '{}_{}'.format(i, j)
            if 0 <= i < m and 0 <= j < n and v not in visited and board[i][j] in temp_tries:
                visited.add(v)
                temp.append(board[i][j])
                _bfs(i-1, j, visited, temp, temp_tries[board[i][j]])
                _bfs(i+1, j, visited, temp, temp_tries[board[i][j]])
                _bfs(i, j-1, visited, temp, temp_tries[board[i][j]])
                _bfs(i, j+1, visited, temp, temp_tries[board[i][j]])

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] in tries:
                    _bfs(row, col, set(), [], tries)
        return result


def main():
    # board = [["a", "b"], ["c", "d"]]
    # words = ["abcb"]
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    solution = Solution()
    result = solution.findWords(board=board, words=words)
    print(result)

if __name__ == '__main__':
    main()




