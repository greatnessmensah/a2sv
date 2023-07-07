class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        alice, you, bob = 0, 0, 0
        n = len(piles) // 3
        piles.sort(reverse=True)
        maxis, minis = piles[:len(piles)-n], piles[len(piles)-n:]
        
        l, r = 0, 0
        
        while l <= len(maxis)-1 and r <= len(minis)-1:
            alice += maxis[l]
            l += 1
            you += maxis[l]
            l += 1
            bob += minis[r]
            r += 1
        
        return you

"""
Time: O(NlogN)
Space: (N+M)
"""
