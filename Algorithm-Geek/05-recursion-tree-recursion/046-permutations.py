# -*- coding: utf-8 -*-


class Solution(object):

    def permute(self, nums: [int]) -> [[int]]:
        results = []
        def sub_permute(numbers, temp):
            if not numbers:
                results.append(temp[:])
            for i in range(len(numbers)):
                temp.append(numbers[i])
                sub_permute(numbers[:i]+numbers[i+1:], temp)
                temp.pop()
        sub_permute(nums, [])
        return results


def main():
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.permute(nums=nums)
    print(result)


if __name__ == '__main__':
    main()

