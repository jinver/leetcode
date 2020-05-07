# You're given a two-dimensional array (a matrix) of potentially unequal height
# and width containing only 0s and 1s. Each
# 0 represents land, and each 1 represents part of a
# river. A river consists of any number of 1s that are either
# horizontally or vertically adjacent (but not diagonally adjacent). The number
# of adjacent 1s forming a river determine its size.


def riverSizes(matrix):
	result = []
    for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			sum = dfs(matrix, i, j)
			if sum > 0:
				result.append(sum)
	return result

def dfs(matrix, i, j):
	if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j] != 1:
		return 0
	matrix[i][j] = '#' # placeholder so we dont double count
	rivers = dfs(matrix, i+1, j) + \
		dfs(matrix, i-1, j) + \
		dfs(matrix, i, j+1) + \
		dfs(matrix, i, j-1)
	return rivers + 1
    