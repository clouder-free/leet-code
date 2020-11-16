# -*- coding: utf-8 -*-

class Solution(object):

    def rotate(self, nums: [int], k: int) -> None:
        k %= len(nums)
        i = 0
        while i < k:
            v = nums[-1]
            for j in range(len(nums)-1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = v
            i += 1

        print(nums)

    def rotate2(self, nums: [int], k: int) -> None:
        k %= len(nums)
        temp = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = temp[i]
        print(nums)


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(nums)
    k = 3
    solution = Solution()
    solution.rotate2(nums=nums, k=k)


if __name__ == '__main__':
    main()