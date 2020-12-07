# -*- coding: utf-8 -*-

class Solution(object):

    def minimumTotal(self, triangle: [[int]]) -> int:
        dp = triangle[-1]
        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col+1])
        return dp[0]


def main():
    triangle = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    solution = Solution()
    result = solution.minimumTotal(triangle=triangle)
    print(result)


if __name__ == '__main__':
    main()



