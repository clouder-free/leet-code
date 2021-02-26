# -*- coding: utf-8 -*-

class Solution(object):

    def minDistance(self, word1: str, word2: str) -> int:
        """动态规划"""
        l1, l2 = len(word1)+1, len(word2)+1
        dp = [[0] * l1 for _ in range(l2)]
        # 第1行
        for i in range(l1):
            dp[0][i] = i
        # 第1列
        for i in range(l2):
            dp[i][0] = i
        for i in range(1, l2):
            for j in range(1, l1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min([dp[i-1][j-1], dp[i-1][j], dp[i][j-1]]) + 1
        return dp[-1][-1]


def main():
    # word1 = 'horse'
    # word2 = 'ros'
    word1 = 'intention'
    word2 = 'execution'
    result = Solution().minDistance(word1=word1, word2=word2)
    print(result)


if __name__ == '__main__':
    main()
