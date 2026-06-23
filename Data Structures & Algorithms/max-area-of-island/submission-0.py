class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # dfs
        def dfs(r,c):
            grid[r][c] = 0 # already visited
            area = 1
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                next_row, next_col = r + dr, c + dc
                if (0 <= next_row < rows and
                    0 <= next_col < cols and
                    grid[next_row][next_col] == 1):
                    area += dfs(next_row, next_col)
            return area

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area