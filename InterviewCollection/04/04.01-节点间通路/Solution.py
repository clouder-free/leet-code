#! /usr/bin/python

class Solution(object):

	def findWhetherExistsPath(self, n: int, graph: [[int]], start: int, target: int) -> bool:
		adj_graph = {}
		for g in graph:
			k, v = g
			if k not in adj_graph:
				adj_graph[k] = []
			adj_graph[k].append(v)
		visited = set()
		nodes = set([start])
		while nodes:
			temp = []
			visited = visited.union(nodes)
			for node in nodes:
				if target in set(adj_graph.get(node, [])):
					return True
				temp.extend([n for n in adj_graph.get(node, []) if n not in visited])
			nodes = set(temp)
		return False

def main():
	# n = 5
	# graph = [[0, 1], [0, 2], [1, 2], [1, 2]]
	# graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]]
	n = 12
	graph = [[0, 1], [1, 2], [1, 3], [1, 10], [1, 11], [1, 4], [2, 4], [2, 6], [2, 9], [2, 10],
	         [2, 4], [2, 5], [2, 10], [3, 7], [3, 7], [4, 5], [4, 11], [4, 11], [4, 10], [5, 7],
	         [5, 10], [6, 8], [7, 11], [8, 10]]
	start = 2
	target = 3
	# start = 0
	# target = 4
	solution = Solution()
	result = solution.findWhetherExistsPath(n=n, graph=graph, start=start, target=target)
	print(result)

if __name__ == "__main__":
	main()
