class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l, r = 0, 0
        res = ""
        
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                res += t[r]
                l += 1
            r += 1
                
        return True if res == s else False

"""
Time: O(N)
Space: O(1)
"""
