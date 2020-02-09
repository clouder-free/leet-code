#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 3
输出: [1,3,3,1]
"""

class Solution(object):

    def getRow(self, rowIndex: int) -> [int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = [1, 1]
        for i in range(2, rowIndex+1):
            temp = []
            j = 0
            while j < len(result) - 1:
                temp.append(result[j] + result[j+1])
                j += 1
            result = [1] + temp[:] + [1]
        return result

def main():
    rowIndex = 3
    solution = Solution()
    result = solution.getRow(rowIndex=rowIndex)
    print(result)

if __name__ == "__main__":
    main()
