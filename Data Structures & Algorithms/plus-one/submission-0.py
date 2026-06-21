class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits          # no carry, done immediately
            digits[i] = 0             # was 9, set to 0 and carry

        return [1] + digits            # all digits were 9 e.g. [9,9,9] → [1,0,0,0]