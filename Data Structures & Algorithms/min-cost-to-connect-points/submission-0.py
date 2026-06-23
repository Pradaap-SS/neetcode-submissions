class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()

        # (cost, point_index)
        min_heap = [(0, 0)]
        total_cost = 0

        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)

            if i in visited:
                continue

            visited.add(i)
            total_cost += cost

            # add all edges from i to unvisited nodes
            for j in range(n):
                if j not in visited:
                    heapq.heappush(min_heap, (dist(i, j), j))

        return total_cost