# -*- coding: utf-8 -*-

class Solution(object):

    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix:
            return False
        # row
        row = -1
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                row = i
                break
        if row == -1:
            return False
        l, r = 0, len(matrix[row])-1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

def main():
    matrix = [[1]]
    target = 1
    solution = Solution()
    result = solution.searchMatrix(matrix=matrix, target=target)
    print(result)

if __name__ == '__main__':
    main()

