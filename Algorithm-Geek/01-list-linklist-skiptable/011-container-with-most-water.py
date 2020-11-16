# -*- coding: utf-8 -*-

class Solution(object):

    def maxArea(self, height: [int]) -> int:
        i, j = 0, len(height) - 1
        result = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            result = max(result, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result


def main():
    # height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # height = [1, 1]
    height = [4, 3, 2, 1, 4]
    solution = Solution()
    result = solution.maxArea(height=height)
    print(result)


if __name__ == '__main__':
    main()



