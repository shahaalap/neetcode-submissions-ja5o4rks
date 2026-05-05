class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        maxheap = []
        self.followers[userId].add(userId)
        
        for f in self.followers[userId]:
            if self.tweets[f]:
                index = len(self.tweets[f]) - 1
                heapq.heappush(maxheap, (-self.tweets[f][index], f, index))

        while len(result) < 10 and maxheap:
            tweet, follower, index = heapq.heappop(maxheap)
            result.append(-tweet)
            if index > 0:
                heapq.heappush(maxheap, (-self.tweets[follower][index-1], follower, index-1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
