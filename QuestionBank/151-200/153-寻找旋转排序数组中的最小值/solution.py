#! /usr/bin/python
# -*- coding: utf8 -*-

class Solution(object):
    
    def findMin(self, nums: [int]) -> int:
        i, j = 0, len(nums)-1
        result = nums[0]
        while i <= j:
            k = (i + j) // 2
            # 左连续
            if nums[i] <= nums[k]:
                if result > nums[i]:
                    result = nums[i]
                i = k + 1
            # 右连续
            else:
                if result > nums[k]:
                    result = nums[k]
                j = k - 1
        return result

def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    solution = Solution()
    result = solution.findMin(nums=nums)
    print(result)

if __name__ == '__main__':
    main()

