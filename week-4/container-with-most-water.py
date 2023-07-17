class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        set two pointers on both ends, compute for the
        area by finding min height and width and update max
        """
        l, r = 0, len(height)-1
        res = 0
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res
    
    """
    Time: O(N)
    Space: O(1)
    """