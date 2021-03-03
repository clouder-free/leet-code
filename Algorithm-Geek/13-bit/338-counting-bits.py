# -*- coding: utf-8 -*-

class Solution(object):

    def countBits(self, num: int) -> [int]:
        result = []
        for i in range(num+1):
            cnt = bin(i).count('1')
            result.append(cnt)
        return result


def main():
    # num = 2
    num = 5
    result = Solution().countBits(num=num)
    print(result)


if __name__ == '__main__':
    main()
