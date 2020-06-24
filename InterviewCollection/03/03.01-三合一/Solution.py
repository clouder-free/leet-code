#! /usr/bin/python

class TripleInOne(object):

	def __init__(self, stackSize: int):
		self.stacks = [[] for _ in range(3)]
		self.stackSize = stackSize

	def push(self, stackNum: int, value: int) -> None:
		if len(self.stacks[stackNum]) < self.stackSize:
			self.stacks[stackNum].append(value)

	def pop(self, stackNum: int) -> int:
		if len(self.stacks[stackNum]) == 0:
			return -1
		return self.stacks[stackNum].pop()

	def peek(self, stackNum: int) -> int:
		if len(self.stacks[stackNum]) == 0:
			return -1
		return self.stacks[stackNum][-1]

	def isEmpty(self, stackNum: int) -> bool:
		return len(self.stacks[stackNum]) == 0

def main():
	tio = TripleInOne(18)
	# print(tio.peek(1))
	# print(tio.pop(2))
	# print(tio.isEmpty(1))
	# print(tio.push(2, 40))
	print("----------")
	# print(tio.pop(2))
	print(tio.push(0, 44))
	# print(tio.push(1, 44))
	print(tio.pop(0))
	# print(tio.push(1, 54))
	print("----------")
	print(tio.push(0, 42))
	print(tio.isEmpty(0))
	# print(tio.pop(1))
	# print(tio.peek(1))
	print(tio.push(0, 56))
	print("----------")
	# print(tio.peek(2))
	print(tio.isEmpty(0))
	# print(tio.peek(2))
	# print(tio.pop(2))
	# print(tio.push(1, 15))
	print("----------")
	# print(tio.isEmpty(1))
	# print(tio.pop(1))
	print(tio.peek(0))
	# print(tio.peek(2))
	print(tio.pop(0))
	print("----------")

if __name__ == "__main__":
	main()

"""
"TripleInOne", "peek", "pop", "isEmpty", "push", 
[18], [1], [2], [1], [2, 40]
"pop", "push", "push", "pop", "push", 
[2], [0, 44], [1, 40], [0], [1, 54], 
"push", "isEmpty", "pop", "peek", "push", 
[0, 42], [0], [1], [1], [0, 56], 
"peek", "isEmpty", "peek", "pop", "push",
[2], [0], [2], [2], [1, 15], 
"isEmpty", "pop", "peek", "peek", "pop", 
[1], [1], [0], [2], [0], 
"""



