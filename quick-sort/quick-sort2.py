#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
快速排序-双路快排
"""

class QuickSort(object):

    def quick_sort(self, nums):
        def partition(nums, l, r):
            i, j = l + 1, r
            while i <= j:
                while nums[i] < nums[l] and i <= j:
                    i += 1
                while nums[j] > nums[l] and i <= j:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[l], nums[j] = nums[j], nums[l]
            return j

        def sort(nums, start, end):
            if start < end:
                p = partition(nums, start, end)
                sort(nums, start, p-1)
                sort(nums, p+1, end)

        sort(nums, 0, len(nums)-1)
        print(nums)

def main():
    nums = [4, 6, 2, 4, 1, 4, 7, 8, 8, 2, 3]
    print(nums)
    qs = QuickSort()
    qs.quick_sort(nums=nums)

if __name__ == "__main__":
    main()

