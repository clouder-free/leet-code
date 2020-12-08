# -*- coding: utf-8 -*-

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.chars = {}
        self.leaf = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for w in word:
            if w not in cur.chars:
                cur.chars[w] = Trie()
            cur = cur.chars[w]
        cur.leaf = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for w in word:
            if w not in cur.chars:
                return False
            cur = cur.chars[w]
        return cur.leaf


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self
        for w in prefix:
            if w not in cur.chars:
                return False
            cur = cur.chars[w]
        return True


def main():
    trie = Trie()

if __name__ == '__main__':
    main()

