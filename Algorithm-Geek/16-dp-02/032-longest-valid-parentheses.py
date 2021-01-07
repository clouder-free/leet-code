# -*- coding: utf-8 -*-


class Solution(object):

    def longestValidParentheses(self, s: str) -> int:
        result = 0
        start, stack = 0, []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                stack.pop()
                if stack:
                    result = i-stack[-1] if i-stack[-1] > result else result
                else:
                    result = i-start+1 if i-start+1 > result else result
            else:
                start = i+1
        return result

    def longestValidParentheses2(self, s: str) -> int:
        # dp[i]代表当前最长匹配长度
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
    solution = Solution()
    result = solution.longestValidParentheses2(s=s)
    print(result)

if __name__ == '__main__':
    main()



