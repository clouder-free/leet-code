#! /usr/bin/python

"""
冒泡排序
扫描一趟 每次操作交换相邻的两者的值
"""

def bubble_sort(nums):
    for i in range(len(nums)):
        flag = False
        for j in range(1, len(nums)-i):
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                flag = True
        # print(nums)
        if not flag:
            break

def main():
    nums = [42, 20, 17, 13, 28, 14, 23, 15]
    # print(nums)
    bubble_sort(nums)
    # print(nums)

if __name__ == "__main__":
    main()
