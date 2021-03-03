# -*- coding: utf-8 -*-

class Solution(object):

    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')


def main():
    n = 0b11111
    result = Solution().hammingWeight(n=n)
    print(result)


if __name__ == '__main__':
    main()
