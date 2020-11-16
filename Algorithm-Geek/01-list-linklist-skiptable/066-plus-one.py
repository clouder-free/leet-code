# -*- coding: utf-8 -*-

class Solution(object):

    def plusOne(self, digits: [int]) -> [int]:
        for i in range(len(digits)-1, -1, -1):
            s = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            if not s:
                break
        return [1] + digits if s else digits

def main():
    digits = [0]
    solution = Solution()
    result = solution.plusOne(digits=digits)
    print(result)

if __name__ == '__main__':
    main()


