class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)] 
        for a, b in prerequisites: 
            adj[a].append(b)

        validCourses = []

        # 0 = unvisited, 1 = visiting (in current path), 2 = visited (safe) 
        state = [0] * numCourses
        
        def dfs(node):
            if state[node] == 1: # cycle detected 
                return False 
            if state[node] == 2: # already confirmed safe 
                return True
            
            state[node] = 1 # mark as visiting     
            for nei in adj[node]: 
                if not dfs(nei): 
                    return False 
            
            state[node] = 2 # mark as safe
            validCourses.append(node) 
            return True

        for i in range(numCourses): 
            if not dfs(i): 
                return [] 
        
        return validCourses
