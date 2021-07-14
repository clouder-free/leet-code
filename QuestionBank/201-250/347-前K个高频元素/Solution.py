# -*- coding: utf-8 -*-
"""
前K个高频元素
"""

class Solution:

    def topKFrequent(self, nums: [int], k: int) -> [int]:
        import heapq
        map_ = {}
        for num in nums:
            map_[num] = map_.get(num, 0) + 1
        # 对频率排序 定义一个小顶堆 大小为k
        queue = []

        for key, v in map_.items():
            heapq.heappush(queue, (v, key))
            if len(queue) > k:
                heapq.heappop(queue)
        # 弹出数据
        result = []
        for i in range(k):
            v = heapq.heappop(queue)[1]
            result.append(v)
        return result[::-1]


def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))


if __name__ == '__main__':
    main()
