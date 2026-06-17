class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # Pacific Ocean
        for c in range(COLS):
            dfs(0, c, pacific)            # top row
            dfs(ROWS - 1, c, atlantic)   # bottom row

        for r in range(ROWS):
            dfs(r, 0, pacific)           # left column
            dfs(r, COLS - 1, atlantic)   # right column

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res