class Twitter:

    def __init__(self):
        self.tweets = []
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []

        for i in range(len(self.tweets) - 1, -1, -1):
            if len(result) == 10:
                break
            if self.tweets[i][1] == userId or self.tweets[i][1] in self.followers[userId]:
                result.append(self.tweets[i][0])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
