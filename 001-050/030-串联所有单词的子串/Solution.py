#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个字符串s和一些长度相同的单词words。
找出s中恰好可以由words中所有单词串联形成的子串的起始位置。
注意子串要与words中的单词完全匹配，中间不能有其他字符，但不需要考虑words中单词串联的顺序。
输入：s = "barfoothefoobarman",  words = ["foo","bar"] 输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
"""

class Solution(object):

    def findSubstring(self, s: str, words: [str]) -> [int]:
        if not s or not words:
            return []
        result = []
        wordict = {}
        for word in words:
            wordict[word] = wordict.get(word, 0) + 1
        wordlen = len(words[0])
        # 按照不同的位置来分组
        for i in range(wordlen):
            left, right = i, i
            currentdict = {}
            while right <= len(s) - wordlen:
                word = s[right:right+wordlen]
                # word是words中的单词
                if word in wordict:
                    # 添加到currentdict中
                    currentdict[word] = currentdict.get(word, 0) + 1
                    # 移动right
                    right += wordlen
                    # 判断该词数量
                    if currentdict[word] > wordict[word]:
                        while currentdict[word] > wordict[word]:
                            leftword = s[left:left+wordlen]
                            currentdict[leftword] -= 1
                            left += wordlen
                    # 判断是否满足要求
                    if currentdict == wordict:
                        result.append(left)
                        leftword = s[left:left+wordlen]
                        currentdict[leftword] -= 1
                        left += wordlen
                # word不是words中的单词
                else:
                    currentdict = {}
                    right += wordlen
                    left = right
        return result

def main():
    # s = "barfoothefoobarman"
    # words = ["foo", "bar"]
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    solution = Solution()
    result = solution.findSubstring(s=s, words=words)
    print(result)

if __name__ == "__main__":
    main()

