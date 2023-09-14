class DataStream:

    def __init__(self, value: int, k: int):
        self.deck = deque()
        self.value = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.deck.append(num)
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        self.deck.popleft()
        
        return self.count >= self.k
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)