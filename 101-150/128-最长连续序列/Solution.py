#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。
输入: [100, 4, 200, 1, 3, 2]  输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""

class Solution(object):

    def longestConsecutive(self, nums: [int]) -> int:
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
                cur_max = num
                cur_min = num - 1
                count = 0
                # 当前连续序列最大值
                while cur_max in nums_dict:
                    count += 1
                    cur_max += 1
                cur_max -= 1
                # 当前连续序列最小值
                while cur_min in nums_dict:
                    count += 1
                    cur_min -= 1
                cur_min += 1
                nums_dict[cur_min] = count
                nums_dict[cur_max] = count
        # 求取当前最大值
        result = 0
        for v in nums_dict.values():
            result = v if v > result else result
        return result

def main():
    nums = [100, 4, 200, 1, 3, 2]
    solution = Solution()
    result = solution.longestConsecutive(nums=nums)
    print(result)

if __name__ == "__main__":
    main()
