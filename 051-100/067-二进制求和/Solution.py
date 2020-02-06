#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。
输入: a = "11", b = "1"  输出: "100"
输入: a = "1010", b = "1011"  输出: "10101"
"""

class Solution(object):

    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        else:
            b = "0" * (len(a) - len(b)) + b
        result = [0] * len(a)
        i = len(a) - 1
        while i > 0:
            s = result[i] + int(a[i]) + int(b[i])
            if s < 2:
                result[i] = s
            else:
                result[i] = s - 2
                result[i-1] += 1
            i -= 1
        s = result[i] + int(a[i]) + int(b[i])
        if s < 2:
            result[i] = s
            return "".join([str(r) for r in result])
        else:
            result[i] = s - 2
            res = [1]
            res.extend(result)
            return "".join([str(r) for r in res])

def main():
    a = "11"
    b = "1111"
    print("a=", a, " b=", b)
    solution = Solution()
    result = solution.addBinary(a=a, b=b)
    print(result)

if __name__ == "__main__":
    main()
