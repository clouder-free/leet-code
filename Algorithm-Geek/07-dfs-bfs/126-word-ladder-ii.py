# -*- coding: utf-8 -*-

class Solution(object):

    def findLadders(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        result = []
        def dfs(wordList, temp):
            if temp[-1] == endWord:
                result.append(temp[:])
                return
            word = temp[-1]
            for i, w in enumerate(word):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nw = word[:i] + c + word[i+1:]
                    if nw in wordList:
                        temp.append(nw)
                        wordList.remove(nw)
                        dfs(wordList, temp)
                        temp.pop()
                        wordList.add(nw)
        dfs(wordList, [beginWord])
        return result


def main():
    beginWord = ''
    endWord = ''
    wordList = []
    solution = Solution()
    result = solution.findLadders(beginWord=beginWord, endWord=endWord, wordList=wordList)
    print(result)


if __name__ == '__main__':
    main()

