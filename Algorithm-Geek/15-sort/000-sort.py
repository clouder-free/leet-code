# -*- coding: utf-8 -*-

"""
比较类排序
    1.交换排序-冒泡排序/快速排序
    2.插入排序-简单插入排序/希尔排序
    3.选择排序-简单选择排序/堆排序
    4.归并排序-二路归并排序/多路归并排序
非比较类排序
    1.计数排序
    2.桶排序
    3.基数排序
"""

def bubbleSort(nums: [int]) -> [int]:
    for i in range(len(nums)):
        flag = True
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = False
        if flag:
            break
    return nums

def quickSort(nums: [int]) -> [int]:
    def quick(nums, i, j):
        if i >= j:
            return
        start, end = i, j
        target = nums[i]
        while start < end:
            # 右半部分第一个小于target
            while start < end and nums[end] > target:
                end -= 1
            nums[start] = nums[end]
            # 左半部分第一个大于target
            while start < end and nums[start] < target:
                start += 1
            nums[end] = nums[start]
        nums[start] = target
        quick(nums, i, start-1)
        quick(nums, start+1, j)
    quick(nums, 0, len(nums)-1)
    return nums

def insertSort(nums: [int]) -> [int]:
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums

def shellSort(nums: [int]) -> [int]:
    step = len(nums) // 2
    while step > 0:
        for i in range(step, len(nums)):
            j = i
            while j-step>=0 and nums[j] < nums[j-step]:
                nums[j-step], nums[j] = nums[j], nums[j-step]
                j -= step
        step //= 2
    return nums

def selectSort(nums: [int]) -> [int]:
    for i in range(len(nums)):
        k = i
        for j in range(i, len(nums)):
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]
    return nums


def heapSort(nums: [int]) -> [int]:
    def _justify(nums, i, length):
        left, right = 2*i+1, 2*i+2
        max_index = i
        if left < length and nums[left] > nums[max_index]:
            max_index = left
        if right < length and nums[right] > nums[max_index]:
            max_index = right
        if max_index != i:
            nums[i], nums[max_index] = nums[max_index], nums[i]
            _justify(nums, max_index, length)
    def _build(nums):
        for i in range(len(nums)//2, -1, -1):
            _justify(nums, i, len(nums))
    # 建立最大堆
    _build(nums)
    length = len(nums)
    # 交换0和-1位置的数据
    for i in range(len(nums)-1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        length -= 1
        _justify(nums, 0, length)
    return nums

def mergeSort(arr):
    def _merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return _merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))


def main():
    nums = [3, 5, 38, 15, 26, 27, 4, 19, 46]
    # res = bubbleSort(nums=nums)
    res = quickSort(nums=nums)
    print('quick:', res)
    res = insertSort(nums=nums)
    print('insert:', res)
    res = shellSort(nums=nums)
    print('shell:', res)
    res = selectSort(nums=nums)
    print('select:', res)
    res = heapSort(nums)
    print('heap:', res)
    res = mergeSort(nums)
    print('merge:', res)


if __name__ == '__main__':
    main()
