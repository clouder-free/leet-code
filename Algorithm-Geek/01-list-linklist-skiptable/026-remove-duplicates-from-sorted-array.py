# -*- coding: utf-8 -*-

class Solution(object):

    def removeDuplicates(self, nums: [int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        print(nums)
        return j+1


def main():
    nums = [1, 1, 2, 4, 5, 6, 6]
    print(nums)
    solution = Solution()
    result = solution.removeDuplicates(nums=nums)
    print(result)


if __name__ == '__main__':
    main()


