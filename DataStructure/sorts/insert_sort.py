#! /usr/bin/python

"""
插入排序
前n-1个数据已经有序 在合适的位置 插入第n个数
"""

def insert_sort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
        print(nums)

def main():
    nums = [42, 20, 17, 13, 28, 14, 23, 15]
    insert_sort(nums)

if __name__ == "__main__":
    main()

