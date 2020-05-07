
from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                flows = []
                self.dfs(i, j, matrix, flows, matrix[i][j])
                # check flows for oceans
                pacific = "N" in flows or "W" in flows
                atlantic = "S" in flows or "E" in flows
                # if Pacific and Atlantic, append to result
                if pacific and atlantic:
                    result.append([i, j])
        return result


    def dfs(self, i, j, matrix, flows, originValue):
        if i<0:
            flows.append("N")
            return
        if i>=len(matrix):
            flows.append("S")
            return
        if j<0:
            flows.append("W")
            return
        if j>=len(matrix[0]):
            flows.append("E")
            return
        if matrix[i][j] == '#': return
        currentValue = matrix[i][j]
        matrix[i][j] = '#'
        if currentValue <= originValue:
            self.dfs(i+1, j, matrix, flows, currentValue)
            self.dfs(i-1, j, matrix, flows, currentValue)
            self.dfs(i, j+1, matrix, flows, currentValue)
            self.dfs(i, j-1, matrix, flows, currentValue)
        matrix[i][j] = currentValue


a = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
result = Solution().pacificAtlantic(a)
