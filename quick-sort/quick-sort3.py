#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
快速排序-三路快排
"""

class QuickSort(object):

    def quick_sort(self, nums):
        def sort(nums, l, r):
            if l >= r:
                return
            i, lt = l+1, l
            j = r + 1
            while i < j:
                # 小于 移到左侧
                if nums[i] < nums[l]:
                    nums[i], nums[lt+1] = nums[lt+1], nums[i]
                    i += 1
                    lt += 1
                # 等于 移动i
                elif nums[i] == nums[l]:
                    i += 1
                # 大于 移到右侧
                else:
                    nums[i], nums[j-1] = nums[j-1], nums[i]
                    j -= 1
            nums[l], nums[lt] = nums[lt], nums[l]
            sort(nums, l, lt-1)
            sort(nums, j, r)

        sort(nums, 0, len(nums)-1)
        print(nums)

def main():
    nums = [4, 6, 2, 4, 1, 4, 7, 8, 8, 2, 3]
    print(nums)
    qs = QuickSort()
    qs.quick_sort(nums=nums)

if __name__ == "__main__":
    main()

