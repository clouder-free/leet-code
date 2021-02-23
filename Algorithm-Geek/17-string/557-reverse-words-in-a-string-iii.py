# -*- coding: utf-8 -*-

class Solution(object):

    def reverseWords(self, s: str) -> str:
        return ' '.join([c[::-1] for c in s.split(' ')])


def main():
    s = 'Let\'s take LeetCode contest'
    r = Solution().reverseWords(s=s)
    print(r)


if __name__ == '__main__':
    main()
