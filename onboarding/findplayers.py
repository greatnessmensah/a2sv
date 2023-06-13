class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = []
        losses = []
        winners = {}
        losers = {}
        hashset = set() 
                
        for i in matches:
            if i[1] not in losers:
                losers[i[1]] = 1
            else:
                losers[i[1]] += 1
            hashset.add(i[0])
            hashset.add(i[1])
                
        for player in hashset:
            if player not in losers:
                wins.append(player)
            elif losers[player] == 1:
                losses.append(player)

        wins.sort()
        losses.sort()
                
        return wins, losses
    
        """
        Time: O(NlogN)
        Space: O(N)
        """
