#! /usr/bin/python

class StackOfPlates(object):

	def __init__(self, cap: int):
		self.stack = []
		self.cap = cap

	def push(self, val: int) -> None:
		if self.stack:
			if len(self.stack[-1]) < self.cap:
				self.stack[-1].append(val)
			else:
				self.stack.append([val])
		elif self.cap > 0:
			self.stack.append([val])

	def pop(self) -> int:
		if self.stack:
			val = self.stack[-1].pop()
			if not self.stack[-1]:
				self.stack = self.stack[:-1]
			return val
		return -1

	def popAt(self, index: int) -> int:
		print(self.stack)
		if len(self.stack) > index:
			val = self.stack[index].pop()
			if not self.stack[index]:
				self.stack = self.stack[:index] + self.stack[index+1:]
			return val
		return -1

def main():
	stack = StackOfPlates(cap=1)
	stack.push(1)
	stack.push(2)
	print(stack.popAt(1))
	print(stack.pop())
	print(stack.pop())

if __name__ == "__main__":
	main()
