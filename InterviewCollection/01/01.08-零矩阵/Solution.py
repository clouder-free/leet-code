#! /usr/bin/python

class Solution(object):

	def setZeroes(self, matrix: [[int]]) -> None:
		rows, cols = set(), set()
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if matrix[i][j] == 0:
					rows.add(i)
					cols.add(j)
		for row in rows:
			matrix[row] = [0] * len(matrix[row])

		for col in cols:
			for i in range(len(matrix)):
				matrix[i][col] = 0
		print(matrix)

def main():
	matrix = [
		[1, 1, 1], [1, 0, 1], [1, 1, 1]
	]
	print(matrix)
	solution = Solution()
	solution.setZeroes(matrix=matrix)

if __name__ == "__main__":
	main()
