# -*- coding: utf-8 -*-

class Solution(object):

    def longestCommonPrefix(self,  strs: [str]) -> str:
        if not strs:
            return ''
        res = ''
        l = min([len(s) for s in strs])
        for i in range(1, l+1):
            prefix = set([s[:i]for s in strs])
            if len(prefix) == 1:
                res = strs[0][:i]
            else:
                break
        return res


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
