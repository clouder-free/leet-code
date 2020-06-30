#! /usr/bin/python

"""
选择排序
每趟扫描 选择最小的值 与当前索引位置的值进行交换
"""

def selection_sort(nums):
    for i in range(len(nums)):
        index = i
        for j in range(i+1, len(nums)):
            if nums[index] > nums[j]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]
        print(nums)

def main():
    nums = [42, 20, 17, 13, 28, 14, 23, 15]
    selection_sort(nums)

if __name__ == "__main__":
    main()