#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
验证给定的字符串是否可以解释为十进制数字。
例如:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。
这里给出一份可能存在于有效十进制数字中的字符列表：
数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
当然，在输入中，这些字符的上下文也很重要。
"""

class Solution(object):

    def isNumber(self, s: str) -> bool:
        if not s or not s.strip():
            return False
        num = False
        e = False
        sign = False
        nume = True
        dot = False
        s = s.strip()
        for i, c in enumerate(s):
            if c == " ":
                return False
            if c == "+" or c == "-":
                if i > 0 and s[i-1] != "e":
                    return False
                sign = True
            elif c.isnumeric():
                num = True
                nume = True
            elif c == ".":
                if dot or e:
                    return False
                dot = True
            elif c == "e":
                if e or not num:
                    return False
                e = True
                nume = False
            else:
                return False
        return num and nume

def main():
    s = "+-1"
    solution = Solution()
    result = solution.isNumber(s=s)
    print(result)

if __name__ == "__main__":
    main()

"""
string s1 = "0"; // True
string s2 = " 0.1 "; // True
string s3 = "abc"; // False
string s4 = "1 a"; // False
string s5 = "2e10"; // True

string s6 = "-e10"; // False
string s7 = " 2e-9 "; // True
string s8 = "+e1"; // False
string s9 = "1+e"; // False
string s10 = " "; // False

string s11 = "e9"; // False
string s12 = "4e+"; // False
string s13 = " -."; // False
string s14 = "+.8"; // True
string s15 = " 005047e+6"; // True

string s16 = ".e1"; // False
string s17 = "3.e"; // False
string s18 = "3.e1"; // True
string s19 = "+1.e+5"; // True
string s20 = " -54.53061"; // True

string s21 = ". 1"; // False
"""

