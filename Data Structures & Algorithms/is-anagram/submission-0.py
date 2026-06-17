class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # --- EARLY EXIT ---
        # If lengths differ, they cannot possibly be anagrams.
        # This also protects us from off-by-one issues in the loop.
        if len(s) != len(t):
            return False

        # --- KEY DATA STRUCTURE ---
        # A fixed-size array of 26 integers, one slot per lowercase letter.
        # Using an array instead of a dict gives O(1) space (bounded to 26),
        # and is faster in practice due to lower overhead.
        count = [0] * 26

        # --- SINGLE PASS THROUGH BOTH STRINGS ---
        # We increment for characters in s and decrement for characters in t.
        # If s and t are anagrams, every increment will be perfectly cancelled
        # by a corresponding decrement, leaving all counts at 0.
        for char_s, char_t in zip(s, t):
            # ord(char) - ord('a') maps 'a'→0, 'b'→1, ..., 'z'→25
            count[ord(char_s) - ord('a')] += 1  # s contributes positively
            count[ord(char_t) - ord('a')] -= 1  # t cancels it out

        # --- FINAL CHECK ---
        # If every character's net count is 0, all characters matched up perfectly.
        # any(count) returns True if any element is non-zero (i.e., a mismatch exists).
        return not any(count)      