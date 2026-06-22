class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate values to simulate max-heap
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            heavy = -heapq.heappop(heap)  # largest
            light = -heapq.heappop(heap)  # 2nd largest

            if heavy != light:
                heapq.heappush(heap, -(heavy - light))

        return -heap[0] if heap else 0
        