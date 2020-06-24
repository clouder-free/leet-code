#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定两个单词word1和word2，计算出将word1转换成word2所使用的最少操作数。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
示例 1:
输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:
输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""

class Solution(object):

    # 动态规划
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l1+1) for _ in range(l2+1)]
        for i in range(l1+1):
            dp[0][i] = i
        for i in range(l2+1):
            dp[i][0] = i
        for i in range(1, l2+1):
            for j in range(1, l1+1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min([dp[i-1][j-1], dp[i-1][j], dp[i][j-1]]) + 1
        return dp[l2][l1]

def main():
    word1 = "horse"
    word2 = "ros"
    solution = Solution()
    result = solution.minDistance(word1=word1, word2=word2)
    print(result)

if __name__ == "__main__":
    main()
