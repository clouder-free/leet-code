#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给出一个区间的集合，请合并所有重叠的区间。
输入: [[1,3],[2,6],[8,10],[15,18]]  输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
输入: [[1,4],[4,5]]  输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

class Solution(object):

    def merge(self, intervals: [[int]]) -> [[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda interval: interval[0])
        i = 1
        while i < len(intervals):
            # 判断是否合并
            if intervals[i-1][0] <= intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][0] = min([intervals[i-1][0], intervals[i][0]])
                intervals[i-1][1] = max([intervals[i-1][1], intervals[i][1]])
                intervals.remove(intervals[i])
            else:
                i += 1
        return intervals

def main():
    intervals = [[1, 4], [0, 2], [3, 5]]
    print(intervals)
    solution = Solution()
    result = solution.merge(intervals=intervals)
    print(result)

if __name__ == "__main__":
    main()

