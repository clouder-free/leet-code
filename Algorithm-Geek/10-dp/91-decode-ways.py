# -*- coding: utf-8 -*-

class Solution(object):

    # dp
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] in ['1', '2']:
                    if i == 1:
                        dp[i] = 1
                    else:
                        dp[i] = dp[i-2]
            else:
                if s[i-1] == '1' or (s[i-1] == '2' and '1' <= s[i] <= '6'):
                    if i == 1:
                        dp[i] = dp[i-1] + 1
                    else:
                        dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[-1]


def main():
    # s = '2101'
    s = '10245'
    solution = Solution()
    result = solution.numDecodings(s=s)
    print(result)


if __name__ == '__main__':
    main()



