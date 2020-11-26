# -*- coding: utf-8 -*-


class Solution(object):

    def generateParenthesis(self, n: int) -> [str]:
        result = []
        def recurise(s, i):
            if len(s) == n * 2:
                result.append(s)
                return
            if i < n:
                recurise(s+'(', i+1)
            if s.count(')') < i:
                recurise(s+')', i)
        recurise('', 0)
        return result


def main():
    n = 3
    solution = Solution()
    result = solution.generateParenthesis(n=n)
    print(result)


if __name__ == '__main__':
    main()



