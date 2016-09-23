class Twitter(object):

    def __init__(self):
        self.maps = {}
        self.friends = {}
        self.index = 0
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.maps:
            self.maps[userId] = []
        self.index += 1
        self.maps[userId].append([tweetId, self.index])

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        feeds = []
        heap = []
        target_users = []
        if userId in self.friends:
            target_users = list(self.friends[userId])
        target_users.append(userId)
        for f in target_users:
            if f in self.maps and self.maps[f]:
                heap.append((-self.maps[f][-1][1], self.maps[f][-1][0], f, 0)) 
        heapq.heapify(heap)
        k = 10
        while k > 0 and heap:
            cur = heapq.heappop(heap)
            feeds.append(cur[1])
            f = cur[2]
            if f in self.maps and self.maps[f]:
                l = len(self.maps[f])
                if cur[3] + 1 < l:
                    heapq.heappush(heap, (-self.maps[f][-1 - cur[3] - 1][1], self.maps[f][-1 - cur[3] - 1][0], cur[2], cur[3] + 1))
            k -= 1
        return feeds

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.friends:
            self.friends[followerId] = set()
        if followerId != followeeId:
            self.friends[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.friends and followeeId in self.friends[followerId]:
            self.friends[followerId].remove(followeeId)
            
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)