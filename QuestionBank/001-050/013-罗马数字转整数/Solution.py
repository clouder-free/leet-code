#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如，罗马数字 2 写做II,即为两个并列的1
12写做XII,即为X+II。
27写做XXVII,即为XX+V+II。
通常情况下，罗马数字中小的数字在大的数字的右边。
但也存在特例，例如4不写做IIII，而是IV。数字1在数字5的左边，所表示的数等于大数5减小数1得到的数值4。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
I可以放在V(5)和X(10)的左边，来表示4和9。
X可以放在L(50)和C(100)的左边，来表示40和90。 
C可以放在D(500)和M(1000)的左边，来表示400和900。
给定一个罗马数字，将其转换成整数。输入确保在1到3999的范围内。
"""

class Solution(object):

    def romanToInt(self, s: str) -> int:
        i = 0
        number = 0
        while i < len(s):
            if s[i] == "M":
                number += 1000
                i += 1
            elif s[i] == "C":
                if i+1 < len(s):
                    if s[i+1] == "M":
                        number += 900
                        i += 2
                    elif s[i+1] == "D":
                        number += 400
                        i += 2
                    else:
                        number += 100
                        i += 1
                else:
                    number += 100
                    i += 1
            elif s[i] == "D":
                number += 500
                i += 1
            elif s[i] == "X":
                if i+1 < len(s):
                    if s[i+1] == "C":
                        number += 90
                        i += 2
                    elif s[i+1] == "L":
                        number += 40
                        i += 2
                    else:
                        number += 10
                        i += 1
                else:
                    number += 10
                    i += 1
            elif s[i] == "L":
                number += 50
                i += 1
            elif s[i] == "V":
                number += 5
                i += 1
            elif s[i] == "I":
                if i+1 < len(s):
                    if s[i+1] == "X":
                        number += 9
                        i += 2
                    elif s[i+1] == "V":
                        number += 4
                        i += 2
                    elif s[i+1] == "I":
                        number += 1
                        i += 1
                else:
                    number += 1
                    i += 1

        return number

def main():
    s = "MCMXCIV"
    solution = Solution()
    result = solution.romanToInt(s=s)
    print(result)

if __name__ == "__main__":
    main()

"""
输入: "III" 输出: 3
输入: "IV" 输出: 4
输入: "IX" 输出: 9
输入: "LVIII" 输出: 58
输入: "MCMXCIV" 输出: 1994
"""
