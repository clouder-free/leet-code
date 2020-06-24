#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):

    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        # 逐个添加元素
        # 空集子集
        results = [[]]
        if not nums:
            return results
        nums.sort()
        last = nums[0]
        size = len(results)
        for num in nums:
            if last != num:
                last = num
                size = len(results)
            start = len(results) - size
            temps = []
            while start < len(results):
                temp = results[start][:]
                temp.append(num)
                temps.append(temp)
                start += 1
            results.extend(temps)
        return results

def main():
    nums = [1, 2, 2]
    solution = Solution()
    result = solution.subsetsWithDup(nums=nums)
    print(result)

if __name__ == "__main__":
    main()



