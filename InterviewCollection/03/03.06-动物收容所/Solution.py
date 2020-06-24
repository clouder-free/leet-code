#! /usr/bin/python

class AnimalShelf(object):

	def __init__(self):
		self.queue = []

	def enqueue(self, animal: [int]) -> None:
		self.queue.append(animal)

	def dequeueAny(self) -> [int]:
		return self.queue.pop(0)

	def dequeueDog(self) -> [int]:
		i = 0
		while i < len(self.queue):
			if self.queue[i][1]:
				return self.queue.pop(i)
			i += 1
		return [-1, -1]

	def dequeueCat(self) -> [int]:
		i = 0
		while i < len(self.queue):
			if not self.queue[i][1]:
				return self.queue.pop(i)
			i += 1
		return [-1, -1]

def main():
	shelf = AnimalShelf()

if __name__ == "__main__":
	main()
