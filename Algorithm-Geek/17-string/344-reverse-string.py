# -*- coding: utf-8 -*-

class Solution(object):

    def reverseString(self, s: [str]) -> None:
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        print(s)



def main():
    s = ['h', 'e', 'l', 'l', 'o']
    print(s)
    Solution().reverseString(s)
    print("Hello World!")


if __name__ == '__main__':
    main()
