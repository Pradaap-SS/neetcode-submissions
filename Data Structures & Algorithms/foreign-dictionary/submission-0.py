class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: build adjacency list with all unique chars
        adj = {c: set() for word in words for c in word}

        # Step 2: compare adjacent words to find ordering rules
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            
            # edge case: prefix word comes after longer word → invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])    # w1[j] comes before w2[j]
                    break                     # only first difference matters!

        # Step 3: topological sort via DFS
        visited = {}   # char → False (visiting) / True (visited)
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]   # False = cycle!

            visited[char] = False      # mark as visiting

            for nei in adj[char]:
                if not dfs(nei):       # cycle detected
                    return False

            visited[char] = True       # mark as fully visited
            res.append(char)           # add to result (reverse order)
            return True

        for char in adj:
            if char not in visited:
                if not dfs(char):
                    return ""          # cycle → invalid

        return "".join(reversed(res))