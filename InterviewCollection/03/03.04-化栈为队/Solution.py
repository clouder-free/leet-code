#! /usr/bin/python

class MyQueue(object):

	def __init__(self):
		"""Initialize your data structure here."""
		self.stack1 = []
		self.stack2 = []

	def push(self, x: int) -> None:
		while self.stack2:
			self.stack1.append(self.stack2.pop())
		self.stack1.append(x)

	def pop(self) -> int:
		while self.stack1:
			self.stack2.append(self.stack1.pop())
		return self.stack1.pop()

	def peek(self) -> int:
		if self.stack1:
			return self.stack1[-1]
		else:
			return self.stack2[0]

	def empty(self) -> bool:
		return True if self.stack1 or self.stack2 else False

def main():
	queue = MyQueue()

if __name__ == "__main__":
	main()
