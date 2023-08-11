class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = defaultdict(int)
        
        for char in s:
            hashmap[char] += 1
          
        even_count = 0
        odd_count = 0
        
        for val in hashmap.values():
            if val % 2 == 0:
                even_count += val
            else:
                odd_count += 1
                even_count += val
        
        return even_count if odd_count <= 1 else even_count - odd_count +1