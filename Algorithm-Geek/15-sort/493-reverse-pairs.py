# -*- coding: utf-8 -*-

class Solution(object):

    def reversePairs(self, nums: [int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j] * 2:
                    result += 1
        return result


def main():
    nums = [1, 3, 2, 3, 1]
    # nums = [2, 4, 3, 5, 1]
    result = Solution().reversePairs(nums=nums)
    print(result)


if __name__ == '__main__':
    main()
