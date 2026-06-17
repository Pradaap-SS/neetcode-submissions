class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # stores indices

        for i, temp in enumerate(temperatures):

            # Resolve previous colder days
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day

            # Current day waits for a warmer day
            stack.append(i)

        return result