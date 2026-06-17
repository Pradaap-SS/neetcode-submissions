class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        # --- BUILD A HASH SET ---
        # O(n) construction. The set gives us O(1) average lookups.
        # Duplicates are automatically removed — they don't affect
        # which sequences exist, only their lengths, which we track separately.
        num_set = set(nums)

        best = 0  # tracks the longest sequence found so far

        for n in num_set:

            # --- SEQUENCE START DETECTION (the critical optimization) ---
            # Only begin counting from n if n is the TRUE start of a sequence,
            # i.e., its left neighbor (n-1) does NOT exist in the set.
            # If n-1 exists, n is in the middle of a longer sequence — skip it.
            # This guarantees each sequence is counted exactly once from its start,
            # giving us O(n) total work across all inner while-loop iterations.
            if (n - 1) not in num_set:

                # n is a sequence start — walk forward as far as possible.
                length = 1
                current = n

                # Keep extending while the next consecutive number exists.
                # Each number is visited here at most once across ALL outer iterations.
                while (current + 1) in num_set:
                    current += 1
                    length += 1

                # Update global best if this sequence is the longest so far.
                best = max(best, length)

        return best    