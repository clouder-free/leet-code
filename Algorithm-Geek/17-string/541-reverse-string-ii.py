# -*- coding: utf-8 -*-

class Solution(object):

    def reversStr(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        for i in range(0, len(s), 2*k):
            # 取出2k个字符
            rs = s[i:i+2*k]
            # 逆转rs的前k个字符
            rs = rs[:k][::-1] + rs[k:]
            # 拼接字符串
            s = s[:i] + rs + s[i+2*k:]
        return s

    def reversStr2(self, s: str, k: int) -> str:
        if not s or k <= 1:
            return s
        for i in range(0, len(s), 2*k):
            s = s[:i] + ''.join(list(s[i:i+k])[::-1]) + s[i+k:]
        return s


def main():
    s = 'abcdefg'
    k = 5
    res = Solution().reversStr(s=s, k=k)
    print('res1:', res)
    res = Solution().reversStr2(s=s, k=k)
    print('res2:', res)


if __name__ == '__main__':
    main()
