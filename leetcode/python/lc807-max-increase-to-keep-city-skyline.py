# In a 2 dimensional array grid, each value grid[i][j] represents the height of a building 
# located there. We are allowed to increase the height of any number of buildings, by any amount 
# (the amounts can be different for different buildings). Height 0 is considered to be a building 
# as well. 

# At the end, the "skyline" when viewed from all four directions of the grid, 
# i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. 
# A city's skyline is the outer contour of the rectangles formed by all the buildings when 
# viewed from a distance. See the following example.

# What is the maximum total sum that the height of the buildings can be increased?


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        iLen = len(grid)
        jLen = len(grid[0])
        score = [[0 for x in range(jLen)] for y in range(iLen)]
        incSkyline = 0
        for i in range(iLen):
            for j in range(jLen):
                hiRow = self.findMaxRow(i, grid)
                hiCol = self.findMaxCol(j, grid)
                hi = min(hiRow, hiCol)
                score[i][j] = hi
                incSkyline += hi - grid[i][j]
        # print(score)
        return incSkyline

    def findMaxRow(self, i, grid):
        hi = 0
        for j in range(len(grid[0])):
            hi = max(hi, grid[i][j])
        return hi

    def findMaxCol(self, j, grid):
        hi = 0
        for i in range(len(grid)):
            hi = max(hi, grid[i][j])
        return hi



grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
s = Solution().maxIncreaseKeepingSkyline(grid)
print(s)
