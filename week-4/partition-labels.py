class Solution(object):
    def partitionLabels(self, s):
        """
        traverse the string to record the last index of each char using a hashmap.
        use a pointer to record end of the current sub string.
        """
        ans = []
        hashmap = {}
        
        for idx, char in enumerate(s):
            hashmap[char] = idx
            
        l, r = 0, 0
        
        for idx, char in enumerate(s):
            r = max(r, hashmap[char])
            if idx == r:
                ans.append(r - l + 1)
                l = r + 1
                
        return ans
    