class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:        
        # --- INTUITION ---
        # As we scan each number, we need to quickly answer: "have I seen this before?"
        # A Hash Set gives us O(1) average-time lookups and insertions,
        # making the entire pass O(n) — optimal for this problem.

        # --- WHY NOT BRUTE FORCE? ---
        # Comparing every pair (two nested loops) is O(n^2), which is too slow
        # for n up to 10^5. The hash set cuts that down to a single O(n) pass.

        # This set will track every number we've encountered so far.
        # seen = set()

        # A set automatically removes duplicates.
        # If the set has fewer elements than the original list,
        # at least one duplicate must have existed.
        # Same O(n) time and O(n) space — just more compact.
        return len(set(nums)) < len(nums)