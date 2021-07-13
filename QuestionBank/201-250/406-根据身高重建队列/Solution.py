# -*- coding: utf-8 -*-
"""
根据身高重建队列
"""

class Solution:

    def reconstructQueue(self, people: [[int]]) -> [[int]]:
        result = []
        # 身高逆序 人数正序
        people = sorted(people, key=lambda p: (-p[0], p[1]))
        for p in people:
            if len(result) < p[1]:
                result.append(p)
            else:
                result.insert(p[1], p)
        return result

def main():
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(Solution().reconstructQueue(people))


if __name__ == '__main__':
    main()
