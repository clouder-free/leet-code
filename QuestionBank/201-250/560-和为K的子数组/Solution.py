# -*- coding: utf-8 -*-
"""
和为K的子数组
"""

class Solution:

    def subarraySum(self, nums: [int], k: int) -> int:
        # 采用前缀和的方式
        if not nums:
            return 0
        result, d = 0, {}
        current = 0
        for num in nums:
            current += num
            if current == k:
                result += 1
            if current - k in d:
                result += d[current-k]
            d[current] = d.get(current, 0) + 1
        return result


def main():
    # nums = [1, 1, 1]
    # nums = [3, 4, 7, 2, -3, 1, 4, 2]
    nums = [1]
    k = 0
    print(Solution().subarraySum(nums, k))


if __name__ == '__main__':
    main()
