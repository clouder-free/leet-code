#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
下图是字符串 s1 = "great" 的一种可能的表示形式。
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。
例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
我们将"rgeat"称作"great"的一个扰乱字符串。
同样地，如果我们继续交换节点"eat"和"at"的子节点，将会产生另一个新的扰乱字符串"rgtae" 。
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
我们将"rgtae”称作"great"的一个扰乱字符串。
给出两个长度相等的字符串s1和s2，判断s2是否是s1的扰乱字符串。
输入: s1 = "great", s2 = "rgeat" 输出: true
输入: s1 = "abcde", s2 = "caebd" 输出: false
"""

class Solution(object):

    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        ls1, ls2 = list(s1), list(s2)
        ls1.sort()
        ls2.sort()
        if ls1 != ls2:
            return False
        length = len(s1)
        for i in range(1, length):
            l1, r1 = s1[:i], s1[i:]
            l2, r2 = s2[:i], s2[i:]
            if self.isScramble(l1, l2) and self.isScramble(r1, r2):
                return True
            l2, r2 = s2[:length-i], s2[length-i:]
            if self.isScramble(l1, r2) and self.isScramble(r1, l2):
                return True
        return False

def main():
    s1 = "abcde"
    s2 = "caebd"
    solution = Solution()
    result = solution.isScramble(s1=s1, s2=s2)
    print(result)

if __name__ == "__main__":
    main()
