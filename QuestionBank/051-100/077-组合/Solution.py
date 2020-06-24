#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution(object):

    def combine(self, n: int, k: int) -> [[int]]:
        results = []
        def sub_combine(n, start, k, nums, results):
            if len(nums) == k:
                results.append(nums[:])
                return
            for i in range(start, n-(k-len(nums))+2):
                nums.append(i)
                sub_combine(n, i+1, k, nums, results)
                nums.pop()

        if n < k or n == 0 or k == 0:
            return results
        nums = []
        sub_combine(n, 1, k, nums, results)
        return results

def main():
    n = 4
    k = 3
    solution = Solution()
    results = solution.combine(n=n, k=k)
    print(results)

if __name__ == "__main__":
    main()
