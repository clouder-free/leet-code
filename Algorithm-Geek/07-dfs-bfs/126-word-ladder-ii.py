# -*- coding: utf-8 -*-

import string

class Solution(object):

    def findLadders(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        # bfs + dfs
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        result = []
        successors = {}
        found = self.__bfs(beginWord, endWord, wordList, successors)
        print(successors)
        if not found:
            return result

        self.__dfs(beginWord, endWord, successors, [beginWord], result)
        return result

    def __bfs(self, beginWord, endWord, wordList, successors):
        found = False
        q = [beginWord]

        visited = set()
        visited.add(beginWord)

        while q:
            temp = []
            next_level_visited = set()
            # 遍历q中的word
            for word in q:
                for i, w in enumerate(word):
                    for j in string.ascii_lowercase:
                        nw = word[:i] + j + word[i+1:]
                        if nw in wordList:
                            if nw not in visited:
                                if nw == endWord:
                                    found = True

                                # 加入下层访问元素
                                if nw not in next_level_visited:
                                    next_level_visited.add(nw)
                                    temp.append(nw)

                                if word not in successors:
                                    successors[word] = set()
                                successors[word].add(nw)

            if found:
                break
            q = temp[:]
            visited |= next_level_visited
        return found

    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        for word in successors.get(beginWord, []):
            self.__dfs(word, endWord, successors, path+[word], res)


def main():
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    solution = Solution()
    result = solution.findLadders(beginWord=beginWord, endWord=endWord, wordList=wordList)
    print(result)


if __name__ == '__main__':
    main()



