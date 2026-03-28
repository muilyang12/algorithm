class Twitter:
    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_followees = defaultdict(set)

        self.global_timer = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((tweetId, self.global_timer))

        self.global_timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        targets = []
        targets.append(self.user_tweets[userId])
        for followee in self.user_followees[userId]:
            targets.append(self.user_tweets[followee])
        target_indices = [0 for _ in range(len(targets))]

        result = []
        heap = []

        for i in range(len(targets)):
            if target_indices[i] >= len(targets[i]):
                continue

            target_index = target_indices[i]
            tweet_id, timer = targets[i][-1 - target_index]
            target_indices[i] += 1

            heapq.heappush(heap, (-timer, tweet_id, i))

        while heap and len(result) < 10:
            _, tweet_id, i = heapq.heappop(heap)
            result.append(tweet_id)

            if target_indices[i] >= len(targets[i]):
                continue

            target_index = target_indices[i]
            tweet_id, timer = targets[i][-1 - target_index]
            target_indices[i] += 1

            heapq.heappush(heap, (-timer, tweet_id, i))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_followees:
            return

        self.user_followees[followerId].remove(followeeId)


"""
The most important question in this problem seems to be about the tweetId. When postTweet is called, the ID is not generated internally but is provided as an integer from the outside.
The critical factor is whether this ID increases over time. If it grows chronologically, we can use it as the sorting key for the Heap. If not, we must introduce an internal timer to
track the order of tweets.

I can definitely feel that this problem is almost identical to "23. Merge k Sorted Lists." The ideas are nearly the same, with the only difference being the way we track the next
elements. In the Linked List version, we can simply access the next element using the next pointer of a Node. However, in this problem, we need to maintain a separate array to keep
track of the current index for each list.
"""
