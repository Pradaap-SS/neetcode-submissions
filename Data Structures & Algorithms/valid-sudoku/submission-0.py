class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # --- THREE SETS OF TRACKERS ---
        # For each of the 9 rows, 9 columns, and 9 boxes, maintain a set of
        # digits seen so far. defaultdict(set) auto-initializes empty sets.
        rows  = defaultdict(set)   # rows[r]          → digits seen in row r
        cols  = defaultdict(set)   # cols[c]          → digits seen in col c
        boxes = defaultdict(set)   # boxes[(br, bc)]  → digits seen in 3×3 box

        # --- SINGLE PASS THROUGH ALL 81 CELLS ---
        for r in range(9):
            for c in range(9):

                digit = board[r][c]

                # Skip empty cells — they don't violate any rule.
                if digit == ".":
                    continue

                # --- BOX INDEX ---
                # Integer division maps each (r,c) to one of 9 box coordinates.
                # Rows 0-2 → box row 0, rows 3-5 → box row 1, rows 6-8 → box row 2.
                # Same logic applies to columns.
                box_key = (r // 3, c // 3)

                # --- DUPLICATE CHECK ---
                # If this digit already appears in the same row, column, OR box,
                # the board is invalid. Check all three constraints simultaneously.
                if (digit in rows[r] or
                    digit in cols[c] or
                    digit in boxes[box_key]):
                    return False

                # --- RECORD THE DIGIT ---
                # No duplicate found — add this digit to all three trackers
                # so future cells in the same row/col/box can detect conflicts.
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box_key].add(digit)

        # All 81 cells passed validation — the board is valid.
        return True       