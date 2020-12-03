# -*- coding: utf-8 -*-

class Solution(object):

    def search(self, nums: [int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1





def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    solution = Solution()
    result = solution.search(nums=nums, target=target)
    print(result)


if __name__ == '__main__':
    main()

