# -*- coding: utf-8 -*-

class Solution:

    def twoSum(self, nums: [int], target: int) -> [int]:
        nd = {}
        for i, n in enumerate(nums):
            m = target - nums[i]
            if m in nd:
                return [nd[m], i]
            nd[n] = i

def main():
    nums = []
    target = 9
    solution = Solution()
    result = solution.twoSum(nums=nums, target=target)
    print(result)

if __name__ == '__main__':
    main()




