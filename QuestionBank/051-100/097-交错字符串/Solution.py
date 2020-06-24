#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定三个字符串s1, s2, s3, 验证s3是否是由s1和s2交错组成的。
示例 1:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
"""

class Solution(object):

    # 动态规划方式求解
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        l1, l2 = len(s1) + 1, len(s2) + 1
        dp = [[False] * l2 for _ in range(l1)]
        dp[0][0] = True
        # 初始化 首行
        for i in range(1, l2):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]
        # 初始化 首列
        for i in range(1, l1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for i in range(1, l1):
            for j in range(1, l2):
                # 左侧/上方
                dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[j-1+i]) or (dp[i-1][j] and s1[i-1] == s3[i-1+j])
        return dp[l1-1][l2-1]

def main():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    solution = Solution()
    result = solution.isInterleave(s1=s1, s2=s2, s3=s3)
    print(result)

if __name__ == "__main__":
    main()

