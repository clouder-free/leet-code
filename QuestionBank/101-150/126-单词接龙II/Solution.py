#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定两个单词（beginWord 和 endWord）和一个字典 wordList，
找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:
如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
输出: []
解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
"""

class Solution(object):

    def findLadders(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        q = {beginWord: {beginWord}}
        z = set()
        wl = len(beginWord)
        begin_set, end_set = {beginWord}, {endWord}
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        i = 1
        while begin_set and end_set:
            i = i + 1
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            nextList = set()
            u = 0
            for word in begin_set:
                for j in range(wl):
                    for k in range(26):
                        nextWord = word[:j] + chr(k + 97) + word[j + 1:]
                        if nextWord in end_set:
                            z.add(nextWord)
                            if (nextWord in q):
                                q[nextWord].add(word)
                            else:
                                q[nextWord] = {word}
                        elif nextWord in wordList:
                            if nextWord in q:
                                q[nextWord].add(word)
                            else:
                                q[nextWord] = {word}
                            if nextWord not in nextList:
                                nextList.add(nextWord)
            for www in nextList:
                wordList.remove(www)
            if z != set():
                return self.g(beginWord, endWord, z, q)  # 因为要求的是最短路径，有结果直接返回就是了
            begin_set = nextList
        return []

    def g(self, beginWord, endWord, z, q):
        for i in q:
            q[i] = list(q[i])
        e = []
        for w in z:
            l = self.f(q, w)  # 将结果相连成小段
            l1 = []
            l2 = []
            for i in l:
                if i[-1] == beginWord:
                    l1.append(i)
                elif i[-1] == endWord:
                    l2.append(i)
                if i[0] == endWord and i[-1] == beginWord:
                    e.append(i[::-1])  # 长度为2
                elif i[0] == beginWord and i[-1] == endWord:
                    e.append(i)
            for a in l1:
                for b in l2:
                    e.append(a[::-1] + b[1:])
        return e

    def f(self, q, word):
        if q[word][0] == word:
            return [[word]]
        e = []
        for i in q[word]:
            for w in self.f(q, i):
                e.append([word] + w)
        return e

def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    result = solution.findLadders(beginWord=beginWord, endWord=endWord, wordList=wordList)
    print(result)

if __name__ == "__main__":
    main()
