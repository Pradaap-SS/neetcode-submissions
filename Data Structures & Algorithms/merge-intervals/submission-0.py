class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])   # sort by start time
        res = [intervals[0]]                  # add first interval

        for i in range(1, len(intervals)):
            curr = intervals[i]
            last = res[-1]                    # last merged interval

            # overlap → merge
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])   # extend end if needed

            # no overlap → add as new interval
            else:
                res.append(curr)

        return res