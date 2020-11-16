# -*- coding: utf-8 -*-

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_stack:
            if self.min_stack[-1] >= x:
                self.min_stack.append(x)
        else:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack:
            x = self.stack.pop()
            if x == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


def main():
    stack = MinStack()

if __name__ == '__main__':
    main()
