#! /usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):

    def convert(self, s: str, numRows: int) -> str:
        string = []
        i = 0
        reverseRows = numRows - 2
        while i < len(s):
            first = s[i:i+numRows]
            string.append(first)
            i += numRows
            if i < len(s) and reverseRows > 0:
                second = s[i:i+reverseRows]
                second += "#" * (reverseRows - len(second))
                second = "#" + second + "#"
                string.append(second[::-1])
                i += reverseRows
        zs = ""
        for i in range(numRows):
            for s in string:
                if i < len(s) and s[i] != "#":
                    zs += s[i]
        return zs

    def convert2(self, s: str, numRows: int) -> str:
        """
        按照周期性 t = numRows * 2 - 2
        如果 i%t > numRows -1 代表是Z的斜行 i位于的行数 t - i%t
        如果 i%t <= numRows -1 代表竖行 i位于的行数 i%t
        """
        if len(s) < numRows or numRows == 1:
            return s
        string = {}
        t = numRows * 2 - 2
        for i, c in enumerate(s):
            # 求行数
            row = t-i%t if i%t>numRows-1 else i%t
            if row not in string:
                string[row] = ""
            string[row] += c

        zs = ""
        for i in range(numRows):
            zs += string[i]
        return zs

    def convert3(self, s: str, numRows: int) -> str:
        if not s or not numRows:
            return ""
        if numRows == 1:
            return s
        
        rows = [""] * min(len(s), numRows)
        i, direction = 0, False
        # direction方向控制输出 True:正向 False:反向
        for c in s:
            rows[i] += c
            if i == 0 or i == numRows - 1:
                direction = bool(1 - direction)
            # i控制每行输出内容 正向:i+1 反向:i-1
            i += 1 if direction else -1

        return "".join(rows)

def main():
    s = "AB"
    numRows = 1
    solution = Solution()
    string = solution.convert3(s=s, numRows=numRows)
    print(string)

if __name__ == "__main__":
    main()
