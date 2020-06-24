#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
示例 1:
输入: "12" 输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:
输入: "226" 输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
"""

class Solution(object):

    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        s = "0" + s
        dp = [1] * len(s)
        for i in range(2, len(s)):
            # 当前字符是否为0
            if s[i] == "0":
                if s[i-1] == "0" or int(s[i-1]) > 2:
                    return 0
                else:
                    dp[i] = dp[i-2]
            # 前一个字符为0
            elif s[i-1] == "0":
                dp[i] = dp[i-1]
            # 两个字符都不为0
            else:
                temp = s[i-1:i+1]
                if 10 < int(temp) <= 26:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        print(dp)
        return dp[-1]

def main():
    s = "226"
    solution = Solution()
    result = solution.numDecodings(s=s)
    print(result)

if __name__ == "__main__":
    main()
