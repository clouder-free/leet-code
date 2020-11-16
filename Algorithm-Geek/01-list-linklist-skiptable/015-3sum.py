# -*- coding: utf-8 -*-

class Solution(object):

    def threeSum(self, nums: [int]) -> [[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while nums[j] == nums[j+1] and j < k:
                        j += 1
                    while nums[k] == nums[k - 1] and j < k:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1


        return result


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    result = solution.threeSum(nums=nums)
    print(result)

if __name__ == '__main__':
    main()



