# -*- coding: utf-8 -*-
"""
除自身以外数组的乘积
"""

class Solution:

    def productExceptSelf(self, nums: [int]) -> [int]:
        # 左右数组乘积法
        l, r = [0]*len(nums), [0]*len(nums)
        # 左数组
        l[0] = 1
        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i-1]
        # 右数组
        r[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            r[i] = r[i+1] * nums[i+1]
        for i in range(len(nums)):
            nums[i] = l[i] * r[i]
        return nums

def main():
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))


if __name__ == '__main__':
    main()
