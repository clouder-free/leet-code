# -*- coding: utf-8 -*-

class Solution(object):

    def reverseWords(self, s: str) -> str:
        # print([c for c in s.strip().split(' ') if c][::-1])
        return ' '.join([c for c in s.strip().split(' ') if c][::-1])


def main():
    s = 'a good   example'
    res = Solution().reverseWords(s=s)
    print(res)


if __name__ == '__main__':
    main()
