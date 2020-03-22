# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take 
# course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return the 
# ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them. 
# If it is impossible to finish all courses, return an empty array.

from collections import defaultdict, deque
from typing import List

class Solution:
    def __init__(self):
        self.isCycle = False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph as adjacency list
        graph = defaultdict(set)
        for dest, src in prerequisites:
            graph[src].add(dest)
            if dest not in graph:
                graph[dest] = set()
        for i in range(numCourses):
            if i not in graph:
                graph[i] = set()
        visited = set()
        queue = deque()
        for vertex in graph:
            self.dfs(vertex, graph, visited, queue)
        if self.isCycle: return []
        return list(queue)

    def dfs(self, vertex, graph, visited, queue):
        if vertex not in visited:
            visited.add(vertex)
            for edge in graph[vertex]:
                self.dfs(edge, graph, visited, queue)
            queue.appendleft(vertex)
        else:
            if vertex not in queue:
                self.isCycle = True




res = Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(res)































