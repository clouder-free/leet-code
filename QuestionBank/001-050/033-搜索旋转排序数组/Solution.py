#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
输入: nums = [4,5,6,7,0,1,2], target = 0 输出: 4
输入: nums = [4,5,6,7,0,1,2], target = 3 输出: -1
"""

class Solution(object):

    def search(self, nums: [int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            print("i:", i, "j:", j, "mid:", mid)
            if target == nums[mid]:
                return mid
            elif nums[mid] < nums[j]:
                # 右半部分有序
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                # 左半部分有序
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            print("i:", i, "j:", j, "mid:", mid)
        return -1

    def search2(self, nums: [int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i+j) // 2
            if nums[mid] == target:
                return mid
            # 左半部分有序
            elif nums[mid] >= nums[i]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            # 右半部分有序
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            print("i:", i, "j:", j, "mid:", mid)
        return -1

def main():
    nums = [3, 1]
    target = 1
    print(nums)
    solution = Solution()
    result = solution.search2(nums=nums, target=target)
    print(result)

if __name__ == "__main__":
    main()

"""
输入: nums = [4,5,6,7,0,1,2], target = 0 输出: 4
输入: nums = [4,5,6,7,0,1,2], target = 3 输出: -1
"""
