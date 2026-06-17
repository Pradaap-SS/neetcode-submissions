class MedianFinder:

    def __init__(self):
        # max heap (left side) -> store negatives
        self.small = []
        # min heap (right side)
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: push into max heap
        heapq.heappush(self.small, -num)

        # Step 2: ensure ordering property
        if self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If one heap has extra element
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        if len(self.large) > len(self.small):
            return float(self.large[0])

        # If even number of elements
        return (-self.small[0] + self.large[0]) / 2.0
        
        