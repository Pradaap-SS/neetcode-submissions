class MedianFinder:

    def __init__(self):
        self.small = []  # max-heap (left half, negated)
        self.large = []  # min-heap (right half)
        

    def addNum(self, num: int) -> None:
        # Step 1: push to small (max-heap)
        heapq.heappush(self.small, -num)

        # Step 2: ensure all of small <= all of large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 3: rebalance sizes (differ by at most 1)
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2.0

        
        