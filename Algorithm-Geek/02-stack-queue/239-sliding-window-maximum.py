# -*- coding: utf-8 -*-

class Solution(object):

    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        result = []
        queue = []
        for i in range(len(nums)):
            while queue and nums[queue[0]] <= nums[i]:
                queue.pop(0)
            queue.insert(0, i)
            if queue[-1] <= i - k:
                queue.pop()
            if i+1 >= k:
                result.append(nums[queue[-1]])
        return result

def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    solution = Solution()
    result = solution.maxSlidingWindow(nums=nums, k=k)
    print(result)

if __name__ == '__main__':
    main()


