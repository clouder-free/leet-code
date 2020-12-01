# -*- coding: utf-8 -*-

class Solution(object):

    def generateParenthesis(self, n: int) -> [str]:
        result = ['(']
        i = 1
        while i < n * 2:
            temp = []
            for res in result:
                if res.count('(') < n:
                    temp.append(res + '(')
                if res.count('(') > res.count(')'):
                    temp.append(res + ')')
            result = temp[:]
            i += 1
        return result


def main():
    n = 3
    solution = Solution()
    result = solution.generateParenthesis(n=n)
    print(result)


if __name__ == '__main__':
    main()



