#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
输入: intervals = [[1,3],[6,9]], newInterval = [2,5] 输出: [[1,5],[6,9]]
输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""

class Solution(object):

    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        if not newInterval:
            return intervals
        start, end = -1, -1
        for i, interval in enumerate(intervals):
            # 区间重叠
            if newInterval[0] <= interval[0] <= newInterval[1] or \
                    newInterval[0] <= interval[1] <= newInterval[1] or \
                    (interval[0] <= newInterval[0] and interval[1] >= newInterval[1]):
                newInterval[0] = min([newInterval[0], interval[0]])
                newInterval[1] = max([newInterval[1], interval[1]])
            # 不重叠
            elif interval[1] < newInterval[0]:
                start = i
            elif interval[0] > newInterval[1]:
                end = i
                break
        # 判断起始位置 结束位置
        if start != -1 and end != -1:
            return intervals[:start+1] + [newInterval] + intervals[end:]
        elif start == -1 and end != -1:
            return [newInterval] + intervals[end:]
        elif start != -1 and end == -1:
            return intervals[:start+1] + [newInterval]
        else:
            return [newInterval]

def main():
    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    # newInterval = [4, 8]
    intervals = [[1, 5]]
    newInterval = [2, 3]
    solution = Solution()
    result = solution.insert(intervals=intervals, newInterval=newInterval)
    print(result)

if __name__ == "__main__":
    main()

