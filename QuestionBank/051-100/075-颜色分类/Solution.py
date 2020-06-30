#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
注意:
不能使用代码库中的排序函数来解决这道题。
示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
"""

class Solution(object):

    def sortColors(self, nums: [int]) -> None:
        # 三路快排
        l, r = 0, len(nums)-1
        i = 0
        while i <= r:
            # 移到左侧
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            # 保持不变
            elif nums[i] == 1:
                i += 1
            # 移到右侧
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
        print(nums)

    def sortColors2(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 红色、白色和蓝色
        red, white, blue = 0, 0, 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        i = 0
        while True:
            if i < red:
                nums[i] = 0
            elif i < red + white:
                nums[i] = 1
            elif i < red + white + blue:
                nums[i] = 2
            else:
                break
            i += 1
        print(nums)

def main():
    nums = [2, 0, 2, 0, 2, 1, 0, 0, 1, 1, 0]
    solution = Solution()
    solution.sortColors(nums=nums)

if __name__ == "__main__":
    main()

