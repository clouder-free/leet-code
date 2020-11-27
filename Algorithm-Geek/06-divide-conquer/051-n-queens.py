# -*- coding: utf-8 -*-

class Solution(object):

    def solveNQueens(self, n: int) -> [[str]]:
        result = []
        if n == 1:
            return [['Q']]
        if n < 4:
            return result
        queens = ['.'*n for _ in range(n)]
        def valid(row, col):
            for i in range(row):
                # 列
                if queens[i][col] == 'Q':
                    return False
                j = queens[i].find('Q')
                if abs(row-i) == abs(col-j):
                    return False
            return True
        def back_trace(k):
            if k == n:
                result.append(queens[:])
                return
            for i in range(n):
                q = queens[k]
                queens[k] = q[:i] + 'Q' + q[i+1:]
                if valid(k, i):
                    back_trace(k+1)
                queens[k] = '.'*n
        back_trace(0)
        return result


def main():
    n = 4
    solution = Solution()
    result = solution.solveNQueens(n=n)
    print(result)


if __name__ == '__main__':
    main()


