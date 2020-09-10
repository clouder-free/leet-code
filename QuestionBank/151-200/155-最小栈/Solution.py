#! /usr/bin/python

"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
"""

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.nums = []
    
    def push(self, x: int):
        self.stack.append(x)
        if self.nums:
            if self.nums[-1] >= x:
                self.nums.append(x)
        else:
            self.nums.append(x)
    
    def pop(self):
        if self.stack:
            x = self.stack.pop()
            if x == self.nums[-1]:
                self.nums.pop()
    
    def top(self):
        if self.stack:
            return self.stack[-1]
    
    def getMin(self):
        if self.stack:
            return self.nums[-1]


def main():
    stack = MinStack()
    stack.push(3)
    stack.pop()
    t = stack.top()
    m = stack.getMin()

if __name__ == '__main__':
    main()





    

