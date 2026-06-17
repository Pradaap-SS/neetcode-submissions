class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # heapq.nlargest finds the k largest by frequency in O(n log k).
        # Preferred when k is very small relative to n.
        return heapq.nlargest(k, count.keys(), key=count.get)