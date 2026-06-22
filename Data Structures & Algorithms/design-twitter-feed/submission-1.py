class Twitter:

    def __init__(self):
        self.count = 0  # global timestamp (higher = more recent)
        self.tweetMap = defaultdict(list)   # userId -> [(timestamp, tweetId)]
        self.followMap = defaultdict(set)   # userId -> {followeeIds}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1  # decrement so most recent = most negative (max-heap trick)
        
    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        maxHeap = []

        # User follows themselves for feed purposes
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # Start from their most recent tweet (last in list)
                idx = len(self.tweetMap[followeeId]) - 1
                timestamp, tweetId = self.tweetMap[followeeId][idx]
                # Push: (timestamp, tweetId, followeeId, index)
                heapq.heappush(maxHeap, (timestamp, tweetId, followeeId, idx - 1))

        while maxHeap and len(result) < 10:
            timestamp, tweetId, followeeId, idx = heapq.heappop(maxHeap)
            result.append(tweetId)

            # If this followee has more tweets, push their next most recent
            if idx >= 0:
                timestamp, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(maxHeap, (timestamp, tweetId, followeeId, idx - 1))

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
