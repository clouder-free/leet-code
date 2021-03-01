# -*- coding: utf-8 -*-

class Solution(object):

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word2)+1, len(word1)+1
        # 二维DP数组
        dp = [[0] * n for _ in range(m)]
        # 首行
        for i in range(1, n):
            dp[0][i] = i
        # 首列
        for i in range(1, m):
            dp[i][0] = i
        # 循环赋值
        for r in range(1, m):
            for l in range(1, n):
                if word2[r-1] == word1[l-1]:
                    dp[r][l] = dp[r-1][l-1]
                else:
                    dp[r][l] = min([dp[r-1][l], dp[r][l-1], dp[r-1][l-1]]) + 1
        return dp[-1][-1]


def main():
    word1 = 'horse'
    word2 = 'ros'
    solution = Solution()
    result = solution.minDistance(word1=word1, word2=word2)
    print(result)


if __name__ == '__main__':
    main()


"""
假设
word1 .....x
word2 .....x
那么编辑距离就是 word1[:-1] word2[:-1]的编辑距离 这样减小了原有问题的规模

word1 .....x
word2 .....y
那么编辑距离就是
min(
word1[:-1] word2
word1 word2[:-1]
word1[:-1] word2[:-1])+一次替换即可 同样减小了原有问题的规模
"""

