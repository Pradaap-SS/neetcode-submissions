class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = n & 1          # extract the last bit
            result |= bit << (31 - i)  # place it in the reversed position
            n >>= 1              # shift n to process next bit
        return result