#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
"""

class Solution(object):

    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        total_nums = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                total_nums.append(nums1[i])
                i += 1
            else:
                total_nums.append(nums2[j])
                j += 1
        if i < len(nums1):
            total_nums.extend(nums1[i:])
        if j < len(nums2):
            total_nums.extend(nums2[j:])

        middle_index = len(total_nums) // 2
        if len(total_nums) % 2 == 0:
            return (total_nums[middle_index] + total_nums[middle_index-1]) / 2
        else:
            return float(total_nums[middle_index])

    def findMedianSortedArrays2(self, nums1: [int], nums2: [int]) -> float:
        i = 0
        j = 0
        left, right = 0, 0
        middle_index = (len(nums1) + len(nums2)) // 2
        while i + j <= middle_index:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    number = nums1[i]
                    i += 1
                else:
                    number = nums2[j]
                    j += 1
            elif i == len(nums1):
                number = nums2[j]
                j += 1
            elif j == len(nums2):
                number = nums1[i]
                i += 1
            else:
                number = 0
            left, right = right, number

        if (len(nums1) + len(nums2)) % 2 == 0:
            return (left + right) / 2
        else:
            return float(right)

    def findMedianSortedArrays3(self, nums1: [int], nums2: [int]) -> float:
        l = (len(nums1) + len(nums2) + 1) // 2
        r = (len(nums1) + len(nums2) + 2) // 2
        return (self.getKth(nums1, 0, nums2, 0, l) + self.getKth(nums1, 0, nums2, 0, r)) / 2
    
    def getKth(self, nums1, start1, nums2, start2, k):
        if start1 > len(nums1) - 1:
            return nums2[start2 + k - 1]
        if start2 > len(nums2) - 1:
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        
        i = min(start1+k//2, len(nums1)) - 1
        j = min(start2+k//2, len(nums2)) - 1
        if nums1[i] > nums2[j]:
            return self.getKth(nums1, start1, nums2, j+1, k-(j-start2+1))
        else:
            return self.getKth(nums1, i+1, nums2, start2, k-(i-start1+1))

def main():
    nums1 = [1, 2]
    nums2 = [3, 4]
    solution = Solution()
    middle = solution.findMedianSortedArrays3(nums1=nums1, nums2=nums2)
    print(middle)

if __name__ == "__main__":
    main()

"""
nums1 = [1, 3]
nums2 = [2]

nums1 = [1, 2]
nums2 = [3, 4]
"""



