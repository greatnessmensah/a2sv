class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        we create a set to check if the current char s[r] is in the current window
        if it is we remove it's last previous occurance s[l] and we keep adding
        new chars, we print the max substring
        """
        hashset = set()
        l = ans = 0
        
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            ans = max(ans, len(hashset))
            
        return ans
        