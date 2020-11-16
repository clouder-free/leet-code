# -*- coding: utf-8 -*-

class Solution(object):

    def moveZeroes(self, nums: [int]) -> None:
        no_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[no_zero_index], nums[i] = nums[i], nums[no_zero_index]
                no_zero_index += 1
        print(nums)


def main():
    nums = [0, 1, 0, 3, 12]
    solution = Solution()
    solution.moveZeroes(nums=nums)


if __name__ == '__main__':
    main()

