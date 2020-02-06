#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""

class Solution(object):

    def plusOne(self, digits: [int]) -> [int]:
        i = len(digits) - 1
        digits[i] += 1
        while i > 0:
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
                i -= 1
            else:
                break
        if i == 0 and digits[i] == 10:
            digits[i] = 0
            result = [1]
            result.extend(digits)
            return result
        return digits

def main():
    solution = Solution()
    digits = [9, 9, 9, 9]
    result = solution.plusOne(digits=digits)
    print(result)

if __name__ == "__main__":
    main()
