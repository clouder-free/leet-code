#! /usr/bin/python
# -*- coding: utf8 -*-

class Solution(object):
    
    # 动态规划求解
    def maxProduct(self, nums: list) -> int:
        result, nmax, nmin = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                nmax, nmin = nmin, nmax
            nmax = max(nums[i], nums[i]*nmax)
            nmin = min(nums[i], nums[i]*nmin)
            result = max(result, nmax)
        return result

def main():
    nums = [2, 3, -2, 4]
    solution = Solution()
    result = solution.maxProduct(nums=nums)
    print(result)

if __name__ == '__main__':
    main()