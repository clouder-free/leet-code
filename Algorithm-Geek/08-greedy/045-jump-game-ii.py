# -*- coding: utf-8 -*-

class Solution(object):

    def jump(self, nums: [int]) -> int:
        pos, end, step = 0, 0, 0
        for i in range(len(nums)-1):
            if pos >= i:
                pos = max(pos, i+nums[i])
                if i == end:
                    end = pos
                    step += 1
        return step


def main():
    nums = []
    solution = Solution()
    result = solution.jump(nums=nums)
    print(result)


if __name__ == '__main__':
    main()


