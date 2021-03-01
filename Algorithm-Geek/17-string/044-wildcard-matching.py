# -*- coding: utf-8 -*-

class Solution(object):

    def isMatch(self, s: str, p: str) -> bool:
        """动态规划"""
        ls, lp = len(s)+1, len(p)+1
        dp = [[False] * ls for _ in range(lp)]
        dp[0][0] = True
        for i in range(1, lp):
            for j in range(ls):
                if p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or (j > 0 and dp[i][j-1])
                elif j > 0 and p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]


def main():
    s = 'aa'
    p = '*'
    result = Solution().isMatch(s=s, p=p)
    print(result)


if __name__ == '__main__':
    main()
