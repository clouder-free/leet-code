#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字2写做II，即为两个并列的1。12写做XII,即为X+II。27写做XXVII,即为XX+V+II。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如4不写做IIII，而是IV。
数字1在数字5的左边，所表示的数等于大数5减小数1得到的数值4。同样地，数字9表示为IX。这个特殊的规则只适用于以下六种情况：
I 可以放在V(5)和X(10) 的左边，来表示4和 9。
X 可以放在L(50)和C(100) 的左边，来表示 40和90。 
C 可以放在D(500)和M(1000) 的左边，来表示400和900。
给定一个整数，将其转为罗马数字。输入确保在1到3999的范围内。
"""

class Solution(object):

    def intToRoman(self, num: int) -> str:
        s = ""
        while num != 0:
            if num >= 1000:
                n = num // 1000
                s += "M" * n
                num = num % 1000
            elif num >= 900:
                s += "CM"
                num = num % 900
            elif num >= 500:
                s += "D"
                num = num % 500
            elif num >= 400:
                s += "CD"
                num = num % 400
            elif num >= 100:
                n = num // 100
                s += "C" * n
                num = num % 100
            elif num >= 90:
                s += "XC"
                num = num % 90
            elif num >= 50:
                s += "L"
                num = num % 50
            elif num >= 40:
                s += "XL"
                num = num % 40
            elif num >= 10:
                n = num // 10
                s += "X" * n
                num = num % 10
            elif num >= 9:
                s += "IX"
                num = num % 9
            elif num >= 5:
                s += "V"
                num = num % 5
            elif num >= 4:
                s += "IV"
                num = num % 4
            elif num >= 1:
                n = num // 1
                s += "I" * n
                num = num % 1

        return s

def main():
    num = 1994
    solution = Solution()
    result = solution.intToRoman(num=num)
    print(result)

if __name__ == "__main__":
    main()

"""
输入: 3 输出: "III"
输入: 4 输出: "IV"
输入: 9 输出: "IX"
输入: 58 输出: "LVIII"
输入: 1994 输出: "MCMXCIV"
"""
