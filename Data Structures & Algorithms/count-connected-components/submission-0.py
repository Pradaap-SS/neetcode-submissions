class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list (undirected)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        components = 0
        for i in range(n):
            if i not in visited:       # found an unvisited node = new component
                dfs(i)
                components += 1        # entire component explored, count it

        return components