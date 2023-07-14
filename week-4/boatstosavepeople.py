class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        count = 0
        people.sort()
        l, r = 0, len(people)-1
        sums = 0
        
        while l <= r:
            if l == r:
                sums = people[l]
            else:
                sums = people[r] + people[l]
                
            if sums <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
                
            count += 1
                
        return count

"""
Time: O(NlogN)
Space: O(1)
"""
