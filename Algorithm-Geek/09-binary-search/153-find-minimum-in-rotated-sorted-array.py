# -*- coding: utf-8 -*-

class Solution(object):

    def findMin(self, nums: [int]) -> int:
        l, r = 0, len(nums)-1
        result = nums[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                if result > nums[l]:
                    result = nums[l]
                l = mid + 1
            else:
                if result > nums[mid]:
                    result = nums[mid]
                r = mid - 1
        return result

def main():
    nums = [3, 4, 5, 1, 2]
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [1]
    solution = Solution()
    result = solution.findMin(nums=nums)
    print(result)

if __name__ == '__main__':
    main()


