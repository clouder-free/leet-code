#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
示例 1:
输入: nums = [2,5,6,0,0,1,2], target = 0 输出: true
示例 2:
输入: nums = [2,5,6,0,0,1,2], target = 3 输出: false
"""

class Solution(object):

    def search(self, nums: [int], target: int) -> bool:
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i+j) // 2
            if target == nums[mid]:
                return True
            elif nums[mid] < nums[j]:
                # 右半部分有序
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            elif nums[mid] > nums[j]:
                # 左半部分有序
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                j -= 1
        return False

def main():
    solution = Solution()
    nums = [2,5,6,0,0,1,2]
    target = 3
    result = solution.search(nums=nums, target=target)
    print(result)

if __name__ == "__main__":
    main()
