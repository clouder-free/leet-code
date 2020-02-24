#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
在一条环路上有N个加油站，其中第i个加油站有汽油gas[i]升。
你有一辆油箱容量无限的的汽车，从第i个加油站开往第i+1个加油站需要消耗汽油cost[i]升。
你从其中的一个加油站出发，开始时油箱为空。
如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
说明: 
如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。
示例 1:
输入: gas  = [1,2,3,4,5] cost = [3,4,5,1,2] 输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
示例 2:
输入: gas  = [2,3,4] cost = [3,4,3] 输出: -1
解释:
你不能从0号或1号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从2号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往0号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往1号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回2号加油站，因为返程需要消耗4升汽油，但是你的油箱只有3升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
"""

class Solution(object):

    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        lg = len(gas)
        for i in range(lg):
            j, next = i, (i+1) % lg
            left = 0
            flag = True
            while next != i:
                if left + gas[j] - cost[j] >= 0:
                    left += gas[j] - cost[j]
                    j, next = next, (next+1) % lg
                else:
                    flag = False
                    break
            if flag:
                if left + gas[j] - cost[j] >= 0:
                    return i
        return -1

def main():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    solution = Solution()
    result = solution.canCompleteCircuit(gas=gas, cost=cost)
    print(result)

if __name__ == "__main__":
    main()




