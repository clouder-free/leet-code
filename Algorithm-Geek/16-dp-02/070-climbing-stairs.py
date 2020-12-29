# -*- coding: utf-8 -*-


class Solution(object):

    mem = {}

    # 递归 每次可以爬1或2个台阶
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 缓存 暂存之前计算的结果
    def climbStairs2(self, n: int) -> int:
        if n not in self.mem:
            if n <= 1:
                self.mem[n] = 1
            else:
                self.mem[n] = self.climbStairs2(n-1) + self.climbStairs2(n-2)
        return self.mem[n]

    # 动态规划DP
    def climbStairs3(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]

    # 滚雪球向前赋值
    def climbStairs4(self, n: int) -> int:
        x, y = 0, 1
        for i in range(n):
            x, y = y, x+y
            # print('n:', i+1, 'y:', y)
        return y

    # 假设每次可以走step步 计算有几种方法
    # 递归
    def climbStairs5(self, n: int, step: int) -> int:
        if n <= 1:
            return 1
        return sum([self.climbStairs5(n-i, step) for i in range(1, step+1) if n >= i])

    # 动态规划DP
    def climbStairs6(self, n: int, step: int) -> int:
        dp = [1, 1]
        for i in range(2, n+1):
            start = i - step if i >= step else 0
            dp.append(sum(dp[start:]))
        return dp[-1]

    # 每次只能走1步或2步 但是前后不能走相同的步伐
    # 递归 使用变量暂存step
    def climbStairs7(self, n: int) -> int:
        def recurse(m, step):
            if m <= 1:
                return 1 if step != 1 else 0
            if step == 1:
                return recurse(m-2, step=2)
            elif step == 2:
                return recurse(m-1, step=1)
        return recurse(n-1, step=1) + recurse(n-2, step=2)


def main():
    n = 3
    solution = Solution()
    result = solution.climbStairs7(n=n)
    print(result)


if __name__ == '__main__':
    main()






