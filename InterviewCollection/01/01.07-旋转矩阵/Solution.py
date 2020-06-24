#! /usr/bin/python

class Solution(object):

	def rotate(self, matrix: [[int]]) -> None:
		for i in range(len(matrix)):
			for j in range(i+1, len(matrix[i])):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

		for row in matrix:
			row.reverse()
		print(matrix)

def main():
	matrix = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
	print(matrix)
	solution = Solution()
	solution.rotate(matrix=matrix)

if __name__ == "__main__":
	main()
