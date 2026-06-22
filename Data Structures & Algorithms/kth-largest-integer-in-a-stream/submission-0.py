class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # If we exceed k elements, remove the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # The smallest in our k-heap = kth largest overall
        return self.heap[0]
        
