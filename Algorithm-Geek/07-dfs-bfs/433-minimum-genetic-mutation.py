# -*- coding: utf-8 -*-

class Solution(object):

    def minMutation(self, start: str, end: str, bank: [str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        changes = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
        q = [start]
        step = 0
        while q:
            temp = []
            for word in q:
                if word == end:
                    return step
                for i, w in enumerate(word):
                    for j in changes[w]:
                        new = word[:i] + j + word[i+1:]
                        if new in bank:
                            temp.append(new)
                            bank.remove(new)
            q = temp[:]
            step += 1
        return -1


def main():
    start = 'AACCGGTT'
    end = 'AACCGCTA'
    bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA']
    solution = Solution()
    result = solution.minMutation(start=start, end=end, bank=bank)
    print(result)


if __name__ == '__main__':
    main()



