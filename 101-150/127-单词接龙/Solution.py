#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定两个单词（beginWord和endWord）和一个字典，
找到从beginWord到endWord的最短转换序列的长度。
转换需遵循如下规则：
每次转换只能改变一个字母。转换过程中的中间单词必须是字典中的单词。
说明:
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
输入: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出: 5
解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
"""
import string

class Solution(object):

    # 广度优先遍历
    def nextWordsList(self, word, wordDict):
        res_list = []
        for i in range(len(word)):
            for j in string.ascii_lowercase:
                new_word = list(word)
                if j != word[i]:
                    new_word[i] = j
                    new_word = ''.join(new_word)
                    if new_word in wordDict:
                        res_list.append(new_word)
                        del wordDict[new_word]
        return res_list

    def bfs(self, beginWord, endWord, wordDict):
        # 返回一个int
        queue = []
        queue.append([beginWord, 1])
        while queue:
            word, step = queue[0][0], queue[0][1]
            queue.pop(0)
            if word == endWord: return step
            # 得到下一次变换一个单词，得到的单词列表
            nextWords = self.nextWordsList(word, wordDict)
            for j in nextWords:
                queue.append([j, step + 1])
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord in wordList: wordList.remove(beginWord)
        wordDict = {}
        for w in wordList: wordDict[w] = 1
        return self.bfs(beginWord, endWord, wordDict)

    # 超时
    def ladderLength2(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        results = []
        if endWord not in wordList:
            return 0
        def diff(word1, word2):
            if word1 == word2:
                return False
            cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    cnt += 1
                    if cnt > 1:
                        return False
            return True
        def ladder(currents, end, words):
            if currents[-1] == end:
                results.append(currents[:])
            elif words:
                for i in range(len(words)):
                    if diff(currents[-1], words[i]):
                        currents.append(words[i])
                        ladder(currents, end, words[:i]+words[i+1:])
                        currents.pop()
        ladder(currents=[beginWord], end=endWord, words=wordList)
        length = 0
        print(results)
        for result in results:
            if length == 0 or len(result) < length:
                length = len(result)
        return length

def main():
    beginWord = "leet"
    endWord = "code"
    wordList = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
    solution = Solution()
    result = solution.ladderLength(beginWord=beginWord, endWord=endWord, wordList=wordList)
    print(result)

if __name__ == "__main__":
    main()
