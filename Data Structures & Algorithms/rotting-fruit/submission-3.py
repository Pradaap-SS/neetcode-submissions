class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        # Deque data structure

        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh+=1

        minutes = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                directions = [(-1,0),(0,-1),(1,0),(0,1)]
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc]=2
                        fresh -= 1
                        q.append((nr,nc))

            minutes+=1
        
        return minutes if fresh == 0 else -1 

