# -*- coding: utf-8 -*-

class Solution(object):

    def numDecoding(self, s: str) -> int:
        if not s or s[0] == '0':
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
                if s[i-1] == '1' or (s[i-1] == '2' and '1' <= s[1] <= '6'):
                    if i == 1:
                        dp[i] = dp[i-1] + 1
                    else:
                        dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[-1]


def main():
    s = '12'
    result = Solution().numDecoding(s=s)
    print(result)


if __name__ == '__main__':
    main()
