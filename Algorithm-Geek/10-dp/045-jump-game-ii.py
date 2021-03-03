# -*- coding: utf-8 -*-

class Solution(object):

    def jump(self, nums: [int]) -> int:
        if nums.count(1) == len(nums):
            return len(nums)-1
        def fun(n):
            if not n:
                return 0
            for k, v in enumerate(n):
                if k + v >= len(n):
                    return fun(n[:k]) + 1
        return fun(nums[:-1])



def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
