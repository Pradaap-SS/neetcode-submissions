class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # We reuse this array for both prefix products (Pass 1)
        # and the final answer (Pass 2), achieving O(1) extra space.
        output = [1] * n

        # ─────────────────────────────────────────────
        # PASS 1: Fill output[i] with the product of all
        # elements STRICTLY TO THE LEFT of index i.
        # output[0] = 1 by definition (nothing to its left).
        # ─────────────────────────────────────────────
        prefix = 1
        for i in range(n):
            output[i] = prefix        # store current running left-product
            prefix *= nums[i]         # extend prefix to include nums[i]
                                      # for the NEXT iteration's left side

        # After Pass 1: output = [1, 1, 2, 8] for nums=[1,2,4,6]

        # ─────────────────────────────────────────────
        # PASS 2: Multiply output[i] (currently the left product)
        # by the product of all elements STRICTLY TO THE RIGHT of i.
        # We track the running right-product in a single variable 'suffix'.
        # ─────────────────────────────────────────────
        suffix = 1
        for i in range(n - 1, -1, -1):  # iterate right to left
            output[i] *= suffix           # combine: left_product × right_product
            suffix *= nums[i]             # extend suffix to include nums[i]
                                          # for the NEXT (leftward) iteration

        # After Pass 2: output = [48, 24, 12, 8] for nums=[1,2,4,6]
        return output    