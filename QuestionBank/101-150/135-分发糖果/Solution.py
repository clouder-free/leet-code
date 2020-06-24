#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
老师想给孩子们分发糖果，有N个孩子站成了一条直线，
老师会根据每个孩子的表现，预先给他们评分。
你需要按照以下要求，帮助老师给这些孩子分发糖果：
每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？
输入: [1,0,2] 输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
输入: [1,2,2] 输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
"""

class Solution(object):

    def candy(self, ratings: [int]) -> int:
        left = [1] * len(ratings)
        right = [1] * len(ratings)
        total = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
            total += max(left[i], right[i])
        total += max(left[-1], right[-1])
        return total

def main():
    ratings = [1, 0, 2]
    solution = Solution()
    result = solution.candy(ratings=ratings)
    print(result)

if __name__ == "__main__":
    main()



