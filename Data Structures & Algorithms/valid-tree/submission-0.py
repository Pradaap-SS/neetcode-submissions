class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

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

        # Start DFS from node 0
        dfs(0)

        # Valid tree only if all nodes were visited (fully connected)
        return len(visited) == n