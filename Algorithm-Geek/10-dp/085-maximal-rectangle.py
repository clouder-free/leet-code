# -*- coding: utf-8 -*-


class Solution(object):

    def largestRectangleArea(self, heights: [int]) -> int:
        result = 0
        stack = []
        i = 0
        while i < len(heights):
            while stack and heights[stack[-1]] >= heights[i]:
                h = stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                result = max(result, width*heights[h])
            stack.append(i)
            i += 1
        if stack:
            last = stack[-1]
            while stack:
                h = stack.pop()
                if stack:
                    width = last - stack[-1]
                else:
                    width = last + 1
                result = max(result, width*heights[h])
        return result

    def maximalRectangle(self, matrix: [[str]]) -> int:
        # m行 n列
        m, n = len(matrix), len(matrix[0])
        rectangles = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0:
                        rectangles[i][j] = 1
                    else:
                        rectangles[i][j] = rectangles[i-1][j] + 1
        areas = [self.largestRectangleArea(row) for row in rectangles]
        return max(areas)


def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    solution = Solution()
    result = solution.maximalRectangle(matrix=matrix)
    print(result)

if __name__ == '__main__':
    main()



