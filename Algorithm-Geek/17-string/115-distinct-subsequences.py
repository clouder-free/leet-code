# -*- coding: utf-8 -*-

class Solution(object):

    def numDistinct(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        dp = [[0] * ls for _ in range(lt)]
        for i in range(lt):
            for j in range(ls):
                if t[i] == s[j]:
                    dp[i][j] = 1 if i == 0 else sum(dp[i-1][:j])
        return sum(dp[-1])



def main():
    s = 'rabbbit'
    t = 'rabbit'
    result = Solution().numDistinct(s=s, t=t)
    print(result)


if __name__ == '__main__':
    main()
