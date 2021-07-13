#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution(object):

    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        i = len(nums) - 2
        while i > -1:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        if i == -1:
            self.reverseNums(nums=nums, i=0, j=len(nums)-1)
            return
        j = len(nums)-1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        self.reverseNums(nums=nums, i=i+1, j=len(nums)-1)
        return nums

    def reverseNums(self, nums, i, j):
        k = i+1
        while k <= j:
            m = k
            temp = nums[m]
            while m > i:
                nums[m] = nums[m-1]
                m -= 1
            nums[m] = temp
            k += 1

    def nextPermutation2(self, nums: [int]) -> None:
        if not nums:
            return
        i = len(nums) - 2
        while i > -1 and nums[i] >= nums[i+1]:
            i -= 1
        if i < 0:
            nums[:] = nums[::-1]
            return
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        print(i, j)
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[len(nums)-1:i:-1]
        return nums

    def nextPermutation3(self, nums: [int]) -> None:
        if not nums or len(nums) == 1:
            return
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        print('i:', i)
        if i >= 0:
            j = len(nums)-1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            print('j:', j)
        print("i+1:", nums[i+1:])
        nums[i+1:] = nums[i+1:][::-1]
        print(nums)


def main():
    nums = [3, 2, 1]
    print(nums[2:-1])
    solution = Solution()
    solution.nextPermutation3(nums=nums)

if __name__ == "__main__":
    main()

"""
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
