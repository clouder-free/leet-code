# -*- coding: utf-8 -*-

class Solution(object):

    def isPower(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 2 == 1:
            return False
        return self.isPower(n//2)


def main():
    n = 218
    result = Solution().isPower(n=n)
    print(result)


if __name__ == '__main__':
    main()
