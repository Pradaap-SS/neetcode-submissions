class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]  # max-heap (negated)
        heapq.heapify(maxHeap)

        time = 0
        # queue stores: (remaining_count, time_when_available)
        queue = deque()

        while maxHeap or queue:
            time += 1

            if maxHeap:
                freq = 1 + heapq.heappop(maxHeap)  # decrement count (negated)
                if freq != 0:
                    queue.append((freq, time + n))  # available again after cooldown

            # If front of queue is ready, push back to heap
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time