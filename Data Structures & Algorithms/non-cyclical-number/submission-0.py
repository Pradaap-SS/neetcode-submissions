class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        seen = set()
        while n != 1:
            if n in seen:
                return False       # cycle detected
            seen.add(n)
            n = sum_of_squares(n)

        return True