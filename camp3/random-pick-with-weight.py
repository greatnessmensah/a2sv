class Solution:
    def __init__(self, w: List[int]):
        self.prefix = [w[0]]

        for c in w[1:]:
            self.prefix.append(self.prefix[-1]+c)

    def pickIndex(self) -> int:
        r = random.randint(1, self.prefix[-1])
        
        return bisect.bisect_left(self.prefix, r)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
