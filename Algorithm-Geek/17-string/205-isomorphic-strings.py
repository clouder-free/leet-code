# -*- coding: utf-8 -*-

class Solution(object):

    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = {}
        st = set()
        for i in range(len(s)):
            # s中未出现的字符
            if s[i] not in sd:
                # 正常映射
                if t[i] not in st:
                    sd[s[i]] = t[i]
                    st.add(t[i])
                # 不同字符 映射到同一字符
                else:
                    return False
            else:
                # 同一字符 映射到不同字符
                if sd[s[i]] != t[i]:
                    return False
        return True


def main():
    s = 'egg'
    t = 'add'
    result = Solution().isIsomorphic(s=s, t=t)
    print(result)


if __name__ == '__main__':
    main()
