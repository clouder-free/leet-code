# -*- coding: utf-8 -*-


class Solution(object):

    def permuteUnique(self, nums: [int]) -> [[int]]:
        results = []
        def sub_permute_unique(numbers, temp):
            if not numbers:
                results.append(temp[:])
                return
            for i in range(len(numbers)):
                if i > 0 and numbers[i] == numbers[i-1]:
                    continue
                temp.append(numbers[i])
                sub_permute_unique(numbers[:i]+numbers[i+1:], temp)
                temp.pop()
        sub_permute_unique(nums, [])
        return results


def main():
    nums = [1, 1, 2]
    solution = Solution()
    result = solution.permuteUnique(nums=nums)
    print(result)

if __name__ == '__main__':
    main()



