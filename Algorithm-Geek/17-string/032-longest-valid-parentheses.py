# -*- coding: utf-8 -*-

class Solution(object):

    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        result = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2
                    if i-2 >= 0:
                        dp[i] += dp[i-2]
                elif dp[i-1] > 0:
                    if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1] + 2
                        if i-dp[i-1]-2 >= 0 and dp[i-dp[i-1]-2] > 0:
                            dp[i] += dp[i-dp[i-1]-2]
                result = max(result, dp[i])
        return result


def main():
    s = '(()'
    result = Solution().longestValidParentheses(s=s)
    print(result)


if __name__ == '__main__':
    main()
