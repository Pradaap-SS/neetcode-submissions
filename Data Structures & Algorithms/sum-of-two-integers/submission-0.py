class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # 32-bit mask to handle negative numbers

        while b & mask:
            carry = (a & b) << 1  # carry bits
            a = a ^ b              # sum without carry
            b = carry

        # if b is 0, return a; handle Python's arbitrary precision for negatives
        return a if b == 0 else a & mask