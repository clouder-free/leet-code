#! /usr/bin/python

"""
希尔排序
通过incr对原数组进行排序 然后不断减小incr 每趟扫描采用插入排序
"""

def shell_sort(nums):
    incr = len(nums) // 2
    while incr >= 1:
        for k in range(incr):
            # 不同组之间采用插入排序
            for i in range(k+incr, len(nums), incr):
                # 单组内采用插入排序
                for j in range(i, k, -incr):
                    if nums[j] < nums[j-incr]:
                        nums[j], nums[j-incr] = nums[j-incr], nums[j]
                    else:
                        break
        print("incr:{} nums:{}".format(incr, nums))
        # 缩小距离
        incr = incr // 2

def main():
    nums = [42, 20, 17, 13, 28, 14, 23, 15]
    shell_sort(nums)

if __name__ == "__main__":
    main()
