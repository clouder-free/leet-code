# -*- coding: utf-8 -*-
"""
回文子串
"""

class Solution:

    def countSubstrings(self, s: str) -> int:
        # 动态规划
        count = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if s[i] == s[j]:
                    dp[i][j] = j-i <= 2 or dp[i+1][j-1]
                    if dp[i][j]:
                        count += 1
        return count

def main():
    # s = 'abc'
    s = 'aaa'
    result = Solution().countSubstrings(s)
    print(result)


if __name__ == '__main__':
    main()
