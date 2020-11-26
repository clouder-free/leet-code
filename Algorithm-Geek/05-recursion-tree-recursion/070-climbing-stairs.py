# -*- coding: utf-8 -*-


class Solution(object):

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f1, f2 = 1, 2
        for i in range(3, n+1):
            f3 = f1 + f2
            f1, f2 = f2, f3
        return f3

def main():
    n = 5
    solution = Solution()
    result = solution.climbStairs(n=n)
    print(result)


if __name__ == '__main__':
    main()



