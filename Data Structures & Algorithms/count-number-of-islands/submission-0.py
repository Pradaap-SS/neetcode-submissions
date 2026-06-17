class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r,c):
            grid[r][c] = 0
            for dr,dc in [[-1,0],[0,-1],[1,0],[0,1]]:
                nr, nc = r+dr,c+dc

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == '1':
                    dfs(nr,nc)
            return


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count+=1
                    dfs(i,j)
        
        return count