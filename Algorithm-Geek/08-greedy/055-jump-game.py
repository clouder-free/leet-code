# -*- coding: utf-8 -*-

class Solution(object):

    def canJump(self, nums: [int]) -> bool:
        if not nums:
            return False
        jumps = [False] * len(nums)
        jumps[-1] = True
        j = len(nums) - 1
        for i in range(j-1, -1, -1):
            if nums[i] >= j - i:
                jumps[i] = True
                j = i
        print(jumps)
        return jumps[0]


def main():
    # nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    solution = Solution()
    result = solution.canJump(nums=nums)
    print(result)


if __name__ == '__main__':
    main()


