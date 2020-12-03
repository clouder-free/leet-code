# -*- coding: utf-8 -*-

class Solution(object):

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        left, right = 1, x // 2
        while left < right:
            mid = (left + right + 1) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                right = mid - 1
            else:
                left = mid
        return left


def main():
    x = 0
    solution = Solution()
    result = solution.mySqrt(x=x)
    print(result)

if __name__ == '__main__':
    main()


