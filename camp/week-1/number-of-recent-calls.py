class RecentCounter:

    def __init__(self):
        self.deck = deque()

    def ping(self, t: int) -> int:
        self.deck.append(t)
        while self.deck[0] < t-3000:
            self.deck.popleft()
            
        return len(self.deck)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)