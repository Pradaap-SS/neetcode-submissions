class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            # Case 1: current interval is completely BEFORE newInterval
            if interval[1] < newInterval[0]:
                res.append(interval)

            # Case 2: current interval is completely AFTER newInterval
            elif interval[0] > newInterval[1]:
                res.append(newInterval)        # insert new first
                res.extend(intervals[i:])     # add all remaining as-is
                return res
            # Case 3: OVERLAP → merge
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        res.append(newInterval)

        return res