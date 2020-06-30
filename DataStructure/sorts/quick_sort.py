#! /usr/bin/python

"""
快速排序
选择一个值作为key值 小于key值在数组左侧 大于等于key值在右侧
然后递归调用两侧的值
"""

def quick_sort(nums, start, end):
    if start >= end:
        return
    
    i, j = start, end
    key = nums[start]
    while i < j:
        # 从右到左 小于key的值
        while i < j and nums[j] >= key:
            j -= 1
        if i < j:
            nums[i] = nums[j]
        # 从左到右 大于key的值
        while i < j and nums[i] < key:
            i += 1
        if i < j:
            nums[j] = nums[i]
    nums[i] = key
    quick_sort(nums, start, i-1)
    quick_sort(nums, i+1, end)


def main():
    nums = [42, 20, 17, 13, 28, 14, 23, 15, 17, 28]
    quick_sort(nums, 0, len(nums)-1)
    print(nums)

if __name__ == "__main__":
    main()

