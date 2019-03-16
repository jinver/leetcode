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