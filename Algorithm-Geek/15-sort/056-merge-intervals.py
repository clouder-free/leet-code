# -*- coding: utf-8 -*-

class Solution(object):

    def merge(self, intervals: [[int]]) -> [[int]]:
        # 排序
        intervals = sorted(intervals, key=lambda i: i[0])
        i = 0
        while i < len(intervals):
            flag = False
            j = i+1
            while j < len(intervals):
                # 区间重叠
                if intervals[i][0] <= intervals[j][0] <= intervals[i][1]:
                    # 合并
                    intervals[i][1] = max(intervals[i][1], intervals[j][1])
                    # 更改intervals
                    intervals = intervals[:j] + intervals[j+1:]
                    flag = True
                else:
                    j += 1
            if flag:
                i = 0
            else:
                i += 1
        return intervals


def main():
    # intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
    intervals = [[1, 4], [4, 5]]
    result = Solution().merge(intervals=intervals)
    print(result)


if __name__ == '__main__':
    main()
