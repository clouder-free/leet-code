# -*- coding: utf-8 -*-

class Solution(object):

    def subsets(self, nums: [int]) -> [[int]]:
        result = [[]]
        for n in nums:
            sub = [[n] + r for r in result]
            result.extend(sub)
        return result

def main():
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.subsets(nums=nums)
    print(result)

if __name__ == '__main__':
    main()

