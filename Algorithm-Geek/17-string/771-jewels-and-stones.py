# -*- coding: utf-8 -*-

class Solution(object):

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([s for s in stones if s in jewels])


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
