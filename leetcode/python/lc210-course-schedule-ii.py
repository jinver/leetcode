# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take 
# course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return the 
# ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them. 
# If it is impossible to finish all courses, return an empty array.


class Solution:
    is_cycle = False

    def findOrder(self, numCourses, prerequisites):
        # Build adjacency list
        adj = {}
        for edge in prerequisites:
            dest, src = edge[0], edge[1]
            if src in adj: adj[src].append(dest)
            else: adj[src] = [dest]
        for i in range(numCourses):
            if i not in adj:
                adj[i] = []
        visited = set()
        stack = []
        for key, val in adj.items():
            if key not in visited:
                self.dfs(key, adj, visited, stack)
        if self.is_cycle: return []
        else: return stack[::-1]

    def dfs(self, key, adj, visited, stack):
            visited.add(key)
            for vertex in adj[key]:
                if vertex not in visited:
                    self.dfs(vertex, adj, visited, stack)
                else:
                    if vertex not in stack:
                        self.is_cycle = True
            stack.append(key)