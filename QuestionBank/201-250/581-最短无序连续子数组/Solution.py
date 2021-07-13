# -*- coding: utf-8 -*-
"""
最短无序连续子数组
"""

class Solution:

    def findUnsortedSubarray(self, nums: [int]) -> int:
        new_nums = nums[::]
        new_nums.sort()
        i, j = 0, len(nums)-1
        while i < j and new_nums[i] == nums[i]:
            i += 1
        while i < j and new_nums[j] == nums[j]:
            j -= 1
        return 0 if i == j else j-i+1


def main():
    nums = [2, 6, 4, 8, 10, 9, 15]
    result = Solution().findUnsortedSubarray(nums)
    print(result)

if __name__ == '__main__':
    print((45-34.92)/45)
    # main()
