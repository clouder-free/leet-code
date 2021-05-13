# -*- coding: utf-8 -*-

class Solution(object):

    def letterCombinations(self, digits: str) -> [str]:
        if not digits:
            return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []
        def sub_letter_combine(dgts, temp):
            if not dgts:
                result.append(''.join(temp))
                return
            value = digit_map[dgts[0]]
            for v in value:
                temp.append(v)
                sub_letter_combine(dgts[1:], temp)
                temp.pop()
        sub_letter_combine(digits, [])
        return result


def main():
    digits = '23'
    solution = Solution()
    result = solution.letterCombinations(digits=digits)
    print(result)

if __name__ == '__main__':
    main()

