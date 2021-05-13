# -*- coding: utf-8 -*-

class Solution(object):

    def majorityElement(self, nums: [int]) -> int:
        length = len(nums)/2.0
        num_map = {}
        for n in nums:
            if n not in num_map:
                num_map[n] = 0
            num_map[n] += 1
            if num_map[n] > length:
                return n

def main():
    nums = [3, 2, 3]
    solution = Solution()
    result = solution.majorityElement(nums=nums)
    print(result)

if __name__ == '__main__':
    main()
