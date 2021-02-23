# -*- coding: utf-8 -*-

class Solution(object):

    def reverseOnlyLetters(self, S: str) -> str:
        chrs = [c for c in S]
        i, j = 0, len(chrs)-1
        while i < j:
            while i < j and not chrs[i].isalpha():
                i += 1
            while i < j and not chrs[j].isalpha():
                j -= 1
            chrs[i], chrs[j] = chrs[j], chrs[i]
            i += 1
            j -= 1
        return ''.join(chrs)


def main():
    # S = 'Test1ng-Leet=code-Q!'
    # S = 'ab-cd'
    S = 'a-bC-dEf-ghIj'
    res = Solution().reverseOnlyLetters(S=S)
    print(res)


if __name__ == '__main__':
    main()
