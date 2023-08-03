class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        left = right = 0
        
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
                right += 1
            else:
                left += 1
                
        return len(t[right:])

"""
Time: O(N+M)
Space: O(1)
"""
