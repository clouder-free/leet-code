# -*- coding: utf-8 -*-

class Solution(object):

    def moveZeros(self, nums: [int]) -> None:
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                j = i + 1
                while j < len(nums):
                    if nums[j] != 0:
                        break
                    j += 1
                if j == len(nums):
                    break
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
        print(nums)

    """快慢指针"""
    def moveZeros2(self, nums: [int]) -> None:
        no_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[no_zero_index] = nums[i]
                no_zero_index += 1
        for i in range(no_zero_index, len(nums)):
            nums[i] = 0
        print(nums)

    def moveZeros3(self, nums: [int]) -> None:
        no_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[no_zero_index], nums[i] = nums[i], nums[no_zero_index]
                no_zero_index += 1
        print(nums)


def main():
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeros3(nums=nums)


if __name__ == '__main__':
    main()


