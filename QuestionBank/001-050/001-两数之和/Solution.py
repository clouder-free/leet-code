#! /usr/bin/python

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

class Solution(object):

    # 1
    def twoSum1(self, nums: [int], target: int) -> [int]:
        for index, value in enumerate(nums):
            anthor_num = target - value
            try:
                anthor_index = nums.index(anthor_num)
                if anthor_index != -1 and anthor_index != index:
                    return [index, anthor_index]
            except Exception as e:
                print("anthor_number:{} Exception:{}".format(anthor_num, repr(e)))
        return []
    # 2
    def twoSum2(self, nums: [int], target: int) -> [int]:
        numbers = [n for n in nums]
        # 对nums排序
        numbers.sort()
        i = 0
        j = len(numbers) - 1
        while True:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] == target:
                m = nums.index(numbers[i])
                n = nums.index(numbers[j], m+1)
                return [m, n]
            else:
                j -= 1
            if i >= j:
                break
        return []

    # 3
    def twoSum3(self, nums: [int], target: int) -> [int]:
        nums_dict = {}
        for index, num in enumerate(nums):
            another = target - num
            if another in nums_dict:
                return [nums_dict[another], index]
            nums_dict[num] = index
        return []

    def twoSum4(self, nums: [int], target: int) -> [int]:
        for index, num in enumerate(nums):
            another = target - num
            if another in nums[index+1:]:
                j = nums[index+1:].index(another)
                return [index, index+j+1]
        return []

def main():
    nums = [4, 2, 5, 4]
    target = 8
    solution = Solution()
    result = solution.twoSum3(nums=nums, target=target)
    print(result)

if __name__ == "__main__":
    main()

"""
数据示例
[2, 7, 11, 15]
[3, 2, 4]
[4, 2, 5, 4]
"""

