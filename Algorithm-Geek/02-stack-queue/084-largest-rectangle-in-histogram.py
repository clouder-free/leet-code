# -*- coding: utf-8 -*-

class Solution(object):

    def largestRectangleArea(self, heights: [int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        result = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                t = stack.pop()
                result = max(result, (i - stack[-1] - 1) * heights[t])
            stack.append(i)
        return result

def main():
    heights = [2, 1, 5, 6, 2, 3]
    solution = Solution()
    result = solution.largestRectangleArea(heights=heights)
    print(result)

if __name__ == '__main__':
    main()



