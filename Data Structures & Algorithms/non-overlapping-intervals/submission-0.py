class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])   # sort by end time
        removes = 0
        prev_end = intervals[0][1]           # end of last kept interval

        for i in range(1, len(intervals)):
            curr = intervals[i]

            # no overlap → keep it, update prev_end
            if curr[0] >= prev_end:
                prev_end = curr[1]

            # overlap → remove current (keep the one with smaller end)
            else:
                removes += 1
                # prev_end stays the same (keeping earlier ending interval)

        return removes 