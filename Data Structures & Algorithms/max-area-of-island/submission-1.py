class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return

        rows, cols = len(grid), len(grid[0])
        
        if 0 < rows > 50 or 0 < cols > 50:
            return

        def dfs(r,c):
            area = 1
            grid[r][c] = 0
            directions = [(-1,0),(0,-1),(1,0),(0,1)]

            for dr,dc in directions:
                nr,nc = r+dr, c+dc

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                    area+=dfs(nr,nc)
            
            return area


        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i,j))

        return maxArea


        

        

        
