#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定两个以字符串形式表示的非负整数num1和num2，返回num1和num2的乘积，
它们的乘积也表示为字符串形式。
输入: num1 = "2", num2 = "3" 输出: "6"
输入: num1 = "123", num2 = "456" 输出: "56088"
num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""

class Solution(object):

    def multiply(self, num1: str, num2: str) -> str:
        base = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        n1, n2 = 0, 0
        for n in num1:
            n1 = n1 * 10 + base[n]
        for n in num2:
            n2 = n2 * 10 + base[n]
        result = n1 * n2
        return str(result)

def main():
    num1 = "123"
    num2 = "456"
    solution = Solution()
    result = solution.multiply(num1=num1, num2=num2)
    print(result)

if __name__ == "__main__":
    main()