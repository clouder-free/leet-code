# -*- coding: utf-8 -*-
"""
寻找重复数
"""

class Solution:

    def findDuplicate(self, nums: [int]) -> int:
        # 快慢指针
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


def main():
    nums = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(nums))
    # print("Hello World!")


if __name__ == '__main__':
    main()
