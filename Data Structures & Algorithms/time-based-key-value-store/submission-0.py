class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # key -> [(timestamp, value)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store[key]
        lo, hi = 0, len(pairs) - 1
        result = ""

        while lo <= hi:
            mid = (lo + hi) // 2
            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1]  # valid candidate, try going right
                lo = mid + 1
            else:
                hi = mid - 1            # too large, go left

        return result
        
