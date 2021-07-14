# -*- coding: utf-8 -*-
"""
数组中第K个最大元素
"""

class Solution:

    def findKthLargest(self, nums: [int], k: int) -> int:
        # 快速排序
        start, end = 0, len(nums)-1
        while True:
            i, j = start, end
            target = nums[i]
            while i < j:
                while i < j and nums[j] > target:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= j:
                    i += 1
                nums[j] = nums[i]
            nums[i] = target
            if i < len(nums) - k:
                start = i+1
            elif i == len(nums) - k:
                return nums[i]
            else:
                end = i-1

def main():
    # nums = [3, 2, 1, 5, 6, 4]
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(Solution().findKthLargest(nums, k))


if __name__ == '__main__':
    main()
