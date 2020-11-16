# -*- coding: utf-8 -*-

class Solution(object):

    def twoSum(self, nums: [int], target: int) -> [int]:
        sum_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in sum_dict:
                return [sum_dict[diff], i]
            else:
                sum_dict[nums[i]] = i


def main():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums=nums, target=target)
    print(result)


if __name__ == '__main__':
    main()




