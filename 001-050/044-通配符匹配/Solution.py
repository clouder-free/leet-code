#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s可能为空，且只包含从a-z的小写字母。
p可能为空，且只包含从a-z的小写字母，以及字符?和*。
输入: s = "aa" p = "a" 输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
输入: s = "aa" p = "*" 输出: true
解释: '*' 可以匹配任意字符串。
输入: s = "cb" p = "?a" 输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
输入: s = "adceb" p = "*a*b" 输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
输入: s = "acdcb" p = "a*c?b" 输出: false
"""

class Solution(object):

    # 动态规划
    def isMatch(self, s: str, p: str) -> bool:
        # 定义dp
        ls = len(s)+1
        lp = len(p)+1
        dp = [[False]*lp for _ in range(ls)]
        # 初始化
        for i in range(ls):
            dp[i][0] = i == 0

        for i in range(ls):
            for j in range(1, lp):
                if p[j-1] == "*":
                    dp[i][j] = (i > 0 and dp[i-1][j]) or dp[i][j-1]
                elif i > 0 and (s[i-1] == p[j-1] or p[j-1] == "?"):
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

def main():
    """
     s = "aa" p = "a"    false
     s = "aa" p = "*"    true
     s = "cb" p = "?a"   false
     s = "adceb" p = "*a*b"  true
     s = "acdcb" p = "a*c?b"  false
    """
    s = "acdcb"
    p = "a*c?b"
    solution = Solution()
    result = solution.isMatch(s=s, p=p)
    print(result)

if __name__ == "__main__":
    main()

"""
状态定义：f(x, y) 字符串s中[0, x-1]范围内的字符串能否匹配字符串p中[0, y-1]范围内的字符串
状态转移：
（1）如果p(y) == '?', f(x, y) = f(x - 1, y - 1)。
（2）如果p(y) == s(x), f(x, y) = f(x - 1, y - 1)。
（3）如果p(y) == '*'，f(x, y) = f(x, y - 1) || f(x - 1, y)。
"""
