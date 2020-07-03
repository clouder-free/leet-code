#! /usr/bin/python

"""
归并排序
分解数组 再合并数列完成归并排序
"""

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    nums = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums.append(left[i])
            i += 1
        else:
            nums.append(right[j])
            j += 1
    while i < len(left):
        nums.append(left[i])
        i += 1
    while j < len(right):
        nums.append(right[j])
        j += 1
    return nums

def main():
    nums = [42, 20, 17, 13, 28, 14, 23, 15]
    nums = merge_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()

