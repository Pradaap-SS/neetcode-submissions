class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # --- KEY DATA STRUCTURE ---
        # Maps each number we've seen so far to its index.
        # This lets us answer "is the complement already in the array?" in O(1).
        seen = {}  # { value: index }

        for i, num in enumerate(nums):

            # --- CORE IDEA ---
            # For the current number, compute what value we'd need to reach the target.
            # If that complement already exists in our map, we've found the pair.
            complement = target - num

            if complement in seen:
                # seen[complement] is always < i because we insert AFTER checking.
                # This guarantees we return [smaller_index, larger_index] automatically.
                return [seen[complement], i]

            # --- INSERT AFTER CHECKING ---
            # We store the current number only after the lookup.
            # This is critical for cases like nums = [5, 5], target = 10:
            # at i=1, we find complement 5 mapped to index 0 (not itself at index 1).
            seen[num] = i

        # The problem guarantees exactly one solution exists,
        # so we will always return inside the loop. This line is unreachable.
        return []