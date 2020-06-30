#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
文本的最后一行应为左对齐，且单词之间不插入额外的空格。
说明:
单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:
输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:
输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:
输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""

class Solution(object):

    def fullJustify(self, words: [str], maxWidth: int) -> [str]:
        if maxWidth == 0:
            return []
        results = []
        temp = []
        i = 0
        while i < len(words):
            if not temp:
                temp.append(words[i])
                i += 1
                continue
            ltemp = len(" ".join(temp))
            if ltemp + len(words[i]) < maxWidth:
                temp.append(words[i])
            else:
                spaces = maxWidth - len("".join(temp))
                # 判断temp中单词数量
                if len(temp) == 1:
                    res = temp[0] + " " * spaces
                else:
                    # 所需空格数
                    even = spaces // (len(temp) - 1)
                    last = spaces % (len(temp) - 1)
                    if last:
                        res = (" "*(even+1)).join(temp[:last]) + " " * (even + 1) + (" "*even).join(temp[last:])
                    else:
                        res = (" " * even).join(temp)

                # 添加到最终结果中
                results.append(res)
                # 重置temp
                temp = []
                temp.append(words[i])
            i += 1
        # 最后的位置
        stemp = " ".join(temp)
        results.append(stemp + " " * (maxWidth - len(stemp)))
        return results

def main():
    # words = ["This", "is", "an", "example", "of", "text", "justification."]
    # words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    words = ["Science","is","what","we","understand","well","enough","to","explain", "to","a","computer.","Art","is","everything","else","we","do"]
    # words = ["Listen", "to", "many,", "speak", "to", "a", "few."]
    maxWidth = 20
    solution = Solution()
    result = solution.fullJustify(words=words, maxWidth=maxWidth)
    print(result)

if __name__ == "__main__":
    main()
