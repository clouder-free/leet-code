#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。
26进制转换
例如，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:
输入: 1
输出: "A"
示例 2:
输入: 28
输出: "AB"
示例 3:
输入: 701
输出: "ZY"
"""


class Solution(object):
    
    def convertToTitle(self, n: int) -> str:
        titles = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        while n > 0:
            n -= 1
            i = n % 26
            result += titles[i]
            n = n // 26
        return result[::-1]


def main():
    n = 52
    solution = Solution()
    result = solution.convertToTitle(n=n)
    print(result)


if __name__ == '__main__':
    main()







