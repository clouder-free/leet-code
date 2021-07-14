# -*- coding: utf-8 -*-
"""
字符串编码
"""

class Solution:

    def decodeString(self, s: str) -> str:
        result, stack = '', []
        i = 0
        while i < len(s):
            if s[i] == '[':
                stack.append(s[i])
            elif s[i] == ']':
                t = stack.pop()
                # pop [
                stack.pop()
                # pop number
                n = stack.pop()
                if stack:
                    if stack[-1] == '[':
                        stack.append(t*int(n))
                    elif stack[-1].isalpha():
                        stack[-1] += t*int(n)
                else:
                    result += t * int(n)
            elif s[i].isalpha():
                if stack:
                    if stack[-1] == '[':
                        stack.append(s[i])
                    else:
                        stack[-1] += s[i]
                else:
                    result += s[i]
            # number
            else:
                if stack and stack[-1].isnumeric():
                    stack[-1] += s[i]
                else:
                    stack.append(s[i])
            i += 1
            print(stack)
        return result

def main():
    # s = '3[a]2[bc]'
    # s = '3[a2[c]]'
    # s = '2[abc]3[cd]ef'
    s = 'abc3[cd]xyz'
    print(Solution().decodeString(s))


if __name__ == '__main__':
    main()
