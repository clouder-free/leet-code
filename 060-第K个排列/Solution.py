#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给出集合[1,2,3,…,n]，其所有元素共有n!种排列。
按大小顺序列出所有排列情况，并一一标记，当n=3时,所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定n和k，返回第k个排列。
说明：
给定n的范围是 [1, 9]。
给定k的范围是[1, n!]。
输入: n=3, k=3  输出: "213"
输入: n=4, k=9  输出: "2314"
"""

class Solution(object):

    def getPermutation(self, n: int, k: int) -> str:
        import math
        lst = [i for i in range(1, n+1)]
        s = ""
        k -= 1
        print("lst:", lst)
        while lst and len(lst) > 0:
            head = k // math.factorial(len(lst) - 1)
            s += str(lst[head])
            k %= math.factorial(len(lst) - 1)
            lst.remove(lst[head])
            print("lst:", lst, "k:", k)
        return s

def main():
    n = 2
    k = 2
    solution = Solution()
    result = solution.getPermutation(n=n, k=k)
    print(result)

if __name__ == "__main__":
    main()

