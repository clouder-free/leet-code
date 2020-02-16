#! /usr/bin/python
# -*- coding: utf-8 -*-

"""


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
