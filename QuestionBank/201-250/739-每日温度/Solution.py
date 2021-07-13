# -*- coding: utf-8 -*-
"""
每日温度
"""

class Solution:

    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        # 循环比较
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            j = i+1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
                j += 1
            if j == len(temperatures):
                result[i] = 0
        return result

    def dailyTemperatures2(self, temperatures: [int]) -> [int]:
        # 单调栈
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                result[top] = i - top
            stack.append(i)
        return result

def main():
    # temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    temperatures = [34, 80, 80, 34, 34, 80, 80, 80, 80, 34]
    result = Solution().dailyTemperatures(temperatures)
    print(result)
    result = Solution().dailyTemperatures2(temperatures)
    print(result)


if __name__ == '__main__':
    main()
