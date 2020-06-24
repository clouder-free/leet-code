#! /usr/bin/python

class SortedStack(object):

	def __init__(self):
		self.stack = []

	def push(self, val: int) -> None:
		temp = []
		while self.stack and self.peek() > val:
			temp.append(self.stack.pop())
		self.stack.append(val)
		while temp:
			self.stack.append(temp.pop())

	def pop(self) -> None:
		if self.stack:
			self.stack.pop()

	def peek(self):
		if self.stack:
			return self.stack[-1]
		return -1

	def isEmpty(self):
		return False if self.stack else True

def main():
	stack = SortedStack()

if __name__ == "__main__":
	main()

