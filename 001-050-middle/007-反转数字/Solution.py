#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意: 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

class Solution(object):

    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        s = str(x)
        flag = 1
        # 判断正负
        if s.startswith("-"):
            flag = -1
            s = s[1:]
        s = s[::-1]
        no_index = 0
        # 第一个不为0的数
        for index, value in enumerate(s):
            if value != "0":
                no_index = index
                break
        s = s[no_index:]
        if -2147483648 <= int(s) * flag <= 2147483648:
            return int(s) * flag
        else:
            return 0

    def reverse2(self, x: int) -> int:
        if x == 0:
            return 0
        s = str(x)
        x = ''
        if s[0] == "-":
            x += "-"
        x += s[::-1].lstrip("0").rstrip("-")
        if -2 ** 31 < int(x) < 2 ** 31 - 1:
            return int(x)
        return 0

def main():
    x = -120
    print(x)
    solution = Solution()
    result = solution.reverse(x=x)
    print(result)

if __name__ == "__main__":
    main()

"""
示例数据
x = 123
x = -120
x = -123
"""