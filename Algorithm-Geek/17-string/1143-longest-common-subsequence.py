# -*- coding: utf-8 -*-

class Solution(object):

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """动态规划来求解"""
        l1, l2 = len(text1)+1, len(text2)+1
        dp = [[0] * l2 for _ in range(l1)]
        for i in range(1, l1):
            for j in range(1, l2):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[-1][-1]


def main():
    text1 = 'abcde'
    text2 = 'ace'
    result = Solution().longestCommonSubsequence(text1=text1, text2=text2)
    print(result)


if __name__ == '__main__':
    main()
