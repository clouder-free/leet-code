# -*- coding: utf-8 -*-


class Solution(object):

    def trap(self, height: [int]) -> int:
        result = 0
        stack = []
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if stack:
                    dis = i - stack[-1] - 1
                    h = min(height[stack[-1]], height[i]) - height[top]
                    result += dis * h
            stack.append(i)
        return result


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solution = Solution()
    result = solution.trap(height)
    print(result)

if __name__ == '__main__':
    main()



