# -*- coding: utf-8 -*-

class Solution(object):

    def maxProduct(self, nums: [int]) -> int:
        max_cur, min_cur, result = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            a, j = max_cur, min_cur
            max_cur = max([nums[i], a*nums[i], j*nums[i]])
            min_cur = min([nums[i], j*nums[i], a*nums[i]])
            result = max(result, max_cur)
        return result


def main():
    # nums = [2, 3, -2, 4]
    nums = [-4, -3, -2]
    solution = Solution()
    result = solution.maxProduct(nums=nums)
    print(result)


if __name__ == '__main__':
    main()


