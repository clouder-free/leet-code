#! /usr/bin/python

class MinStack(object):

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack = []

	def push(self, x: int) -> None:
		if self.stack and self.stack[-1][1] <= x:
			self.stack.append([x, self.stack[-1][1]])
		else:
			self.stack.append([x, x])

	def pop(self) -> None:
		if self.stack:
			self.stack.pop()

	def top(self) -> int:
		return self.stack[-1][0]

	def getMin(self) -> int:
		return self.stack[-1][1]

def main():
	stack = MinStack()

if __name__ == "__main__":
	main()
