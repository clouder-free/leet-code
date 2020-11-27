# -*- coding: utf-8 -*-

class Solution(object):

    def combine(self, n: int, k: int) -> [[int]]:
        result = []
        def recurse(nums, temp):
            if len(temp) == k:
                result.append(temp[:])
                return
            for i in range(len(nums)):
                temp.append(nums[i])
                recurse(nums[i+1:], temp)
                temp.pop()
        numbers = list(range(1, n+1))
        recurse(numbers, [])
        return result

def main():
    n = 4
    k = 2
    solution = Solution()
    result = solution.combine(n=n, k=k)
    print(result)

if __name__ == '__main__':
    main()



