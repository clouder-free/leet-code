# -*- coding: utf-8 -*-

class Solution(object):

    def generateParenthesis(self, n: int) -> [str]:
        if n == 1:
            return ['()']
        result = []
        def generate(s):
            if len(s) == 2*n:
                result.append(s)
                return
            if s.count('(') < n:
                generate(s+'(')
            if s.count('(') > s.count(')'):
                generate(s+')')
        generate('')
        return result


def main():
    n = 2
    result = Solution().generateParenthesis(n=n)
    print(result)


if __name__ == '__main__':
    main()
