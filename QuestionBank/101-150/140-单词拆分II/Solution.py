#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个非空字符串s和一个包含非空单词列表的字典wordDict，
在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: []
"""

class Solution(object):

    def wordBreak(self, s, wordDict):
        res = []
        memo = dict()
        return self.dfs(s, res, wordDict, memo)

    def dfs(self, s, res, wordDict, memo):
        # 如果当前单词存在于字典中，直接返回
        if s in memo:
            return memo[s]
        # 当前字符串的为空判断
        if not s:
            return [""]

        # 拼接存在于字典中的字符串
        res = []
        for word in wordDict:
            if s[:len(word)] != word:
                continue
            for r in self.dfs(s[len(word):], res, wordDict, memo):
                res.append(word + ("" if not r else " " + r))
        memo[s] = res
        return res

def main():
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    solution = Solution()
    result = solution.wordBreak(s=s, wordDict=wordDict)
    print(result)

if __name__ == "__main__":
    main()


