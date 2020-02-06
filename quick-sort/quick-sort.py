#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
快速排序
1.找到分割点
2.递归排序左半部分和右半部分
"""

class QuickSort(object):

    def quick_sort(self, nums):
        def partition(nums, l, r):
            i = l - 1
            j = l
            while j < r:
                if nums[j] <= nums[r]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            nums[i+1], nums[r] = nums[r], nums[i+1]
            return i + 1

        def sort(nums, start, end):
            if start < end:
                p = partition(nums, start, end)
                sort(nums, start, p-1)
                sort(nums, p+1, end)

        # 执行数据
        sort(nums, 0, len(nums)-1)
        print(nums)

def main():
    nums = [4, 6, 2, 3, 1, 5, 7, 8]
    print(nums)
    qs = QuickSort()
    qs.quick_sort(nums=nums)

if __name__ == "__main__":
    main()

