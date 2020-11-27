# -*- coding: utf-8 -*-

class Solution(object):

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return 1 / self.myPow(x*x, n//2) * x
        else:
            return 1 / self.myPow(x*x, n//2)


def main():
    x = 2.1
    n = 3
    solution = Solution()
    result = solution.myPow(x=x, n=n)
    print(result)

if __name__ == '__main__':
    main()


