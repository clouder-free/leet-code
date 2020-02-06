#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
注意：整数序列中的每一项将表示为一个字符串。
输入: 1 输出: "1"
输入: 4 输出: "1211"
"""

class Solution(object):

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        last = self.countAndSay(n-1)
        i = 0
        s = ""
        k = 1
        while i < len(last):
            if i+1 < len(last) and last[i] == last[i+1]:
                k += 1
            else:
                s += str(k) + last[i]
                k = 1
            i += 1
        return s

def main():
    n = 8
    solution = Solution()
    result = solution.countAndSay(n=n)
    print(result)

if __name__ == "__main__":
    main()

"""
"""
