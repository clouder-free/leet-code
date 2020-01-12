#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

class Solution(object):

    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        results = []
        candidates.sort()
        def DFS(candidates, target, start, answer, results):
            if target > 0:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    answer.append(candidates[i])
                    DFS(candidates, target-candidates[i], i+1, answer, results)
                    answer.pop()
            elif target == 0:
                temp = answer[:]
                results.append(temp)
                return
            else:
                return
        DFS(candidates, target, 0, [], results)
        return results

def main():
    candidates = [2, 5, 2, 1, 2]
    target = 5
    solution = Solution()
    result = solution.combinationSum2(candidates=candidates, target=target)
    print(result)

if __name__ == "__main__":
    main()

"""
"""
