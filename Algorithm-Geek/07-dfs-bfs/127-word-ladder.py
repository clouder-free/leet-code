# -*- coding: utf-8 -*-

class Solution(object):

    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        words = [beginWord]
        step = 1
        while words:
            temp = []
            for word in words:
                if word == endWord:
                    return step
                for i, w in enumerate(word):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nw = word[:i] + c + word[i+1:]
                        if nw in wordList:
                            temp.append(nw)
                            wordList.remove(nw)
            step += 1
            words = temp[:]
        return 0


def main():
    beginWord = ''
    endWord = ''
    wordList = []
    solution = Solution()
    result = solution.ladderLength(beginWord=beginWord, endWord=endWord, wordList=wordList)
    print(result)


if __name__ == '__main__':
    main()

