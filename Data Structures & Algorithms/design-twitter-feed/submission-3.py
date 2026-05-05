class Twitter:

    def __init__(self):
        self.tweets = []
        self.followers = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        listofUsers = [f[1] for f in self.followers if f[0] == userId]
        listofUsers.append(userId)

        for i in range(len(self.tweets) - 1, -1, -1):
            if len(result) == 10:
                break
            if self.tweets[i][1] in listofUsers:
                result.append(self.tweets[i][0])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if (followerId, followeeId) not in self.followers:
            self.followers.append((followerId, followeeId))
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId, followeeId) in self.followers:
            node = self.followers.index((followerId, followeeId))
            self.followers.pop(node)
        
