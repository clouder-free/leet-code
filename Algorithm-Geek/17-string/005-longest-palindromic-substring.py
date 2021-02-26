# -*- coding: utf-8 -*-



class Solution(object):

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        dp = [[False] * len(s) for _ in range(len(s))]
        l, r = 0, 0
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    # 对应aba 或者aa bb这种子串
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    if dp[i][j] and r-l < j-i:
                        l, r = i, j
        return s[l:r+1]


def main():
    # s = 'babad'
    s = 'cbbd'
    res = Solution().longestPalindrome(s=s)
    print(res)


if __name__ == '__main__':
    main()
