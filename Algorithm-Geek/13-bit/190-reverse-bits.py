# -*- coding: utf-8 -*-

class Solution(object):

    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret



def main():
    n = 100
    result = Solution().reverseBits(n=n)
    print(result)


if __name__ == '__main__':
    main()
