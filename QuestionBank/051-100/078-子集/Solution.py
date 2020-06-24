#! /usr/bin/python
# -*- coding: utf-8 -*-

"""


"""

class Solution(object):

    def subsets(self, nums: [int]) -> [[int]]:
        # 逐个添加元素
        # 空集子集
        results = [[]]
        for num in nums:
            # print("before:", results, "num:", num)
            temp = [sub + [num] for sub in results]
            results.extend(temp)
            # print("after:", results)
        # print("last:", results)
        return results

    def subsets2(self, nums: [int]) -> [[int]]:
        def subset(nums, k, temp, results):
            if len(temp) == k:
                results.append(temp[:])
                return
            for n in range(len(nums)):
                temp.append(nums[n])
                bak = nums[n+1:]
                subset(bak, k, temp, results)
                temp.pop()

        # 空集
        results = [[]]
        # 子集
        i = 1
        while i < len(nums):
            temp = []
            subset(nums, i, temp, results)
            i += 1
        # 全集
        results.append(nums)
        return results


def main():
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.subsets(nums=nums)
    print(result)

if __name__ == "__main__":
    main()
