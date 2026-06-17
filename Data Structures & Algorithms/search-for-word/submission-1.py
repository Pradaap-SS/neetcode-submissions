class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):          # all characters matched
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False            # out of bounds
            if board[r][c] != word[i]:  # wrong character
                return False
            if board[r][c] == '#':      # already visited
                return False

            temp = board[r][c]
            board[r][c] = '#'           # mark visited

            found = (dfs(r+1, c, i+1) or
                    dfs(r-1, c, i+1) or
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1))

            board[r][c] = temp          # unmark (backtrack)
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False