#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定两个有序整数数组nums1和nums2，将nums2合并到nums1中，使得num1成为一个有序数组。
说明:
初始化nums1和nums2的元素数量分别为m和n。
你可以假设nums1有足够的空间（空间大小大于或等于m+n）来保存nums2中的元素。
示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
"""

class Solution(object):

    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m and j < n:
            if nums2[j] < nums1[i]:
                # 移动元素赋值
                k = m
                while k > i:
                    nums1[k] = nums1[k-1]
                    k -= 1
                nums1[k] = nums2[j]
                j += 1
                m += 1
            i += 1

        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1
        print(nums1)

def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    print(nums1)
    solution = Solution()
    solution.merge(nums1=nums1, m=m, nums2=nums2, n=n)

if __name__ == "__main__":
    main()

