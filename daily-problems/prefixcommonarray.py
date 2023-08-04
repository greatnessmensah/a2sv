class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        count elements in A and B alternatively
        append the count of 2 in hashmap.values()
        """
        res = []
        hashmap = defaultdict(int)
        
        
        for idx in range(len(A)):
            hashmap[A[idx]] += 1
            hashmap[B[idx]] += 1
            
            res.append(hashmap.values().count(2))
            
        return res

"""
Time: O(N^2)
Space: O(N)
"""
