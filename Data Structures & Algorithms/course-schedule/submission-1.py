class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)

        # 0 = unvisited, 1 = visiting (in current path), 2 = visited (safe)
        state = [0] * numCourses
        def dfs(node):
            if state[node] == 1:   # cycle detected
                return False
            if state[node] == 2:   # already confirmed safe
                return True
            state[node] = 1        # mark as visiting
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            state[node] = 2        # mark as safe
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
