class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        next_odd = prev_odd = -1
        left = 0
        
        get idx's of odds elems
        number of even numbers to the right is going to be next_odd - right
        number of even numbers to the left is going to be left - previous_odd
        
        if difference of right and left = k-1 -> total is left * right
        
        [1,1,2,1,1]
        3
        
        [0,1,3,4]
        [l   r] -> odds[r] - odds[l] == k-1
                   total += left * right
                   total == 0
                   
        [0,1,3,4]   
           [l  r] - left_even = 1, right_even = 2
                    
                    odds[right] - odds[left] == k-1
                    total += left * right
                    total == 2
                    
        
        
        """
        odds = [idx for idx in range(len(nums)) if nums[idx] % 2]
        prev_odd = -1
        
        left = total = left_even = right_even = 0
        
        for right in range(len(odds)):
            if left - 1 >= 0:
                prev_odd = odds[left-1]
            left_even = odds[left] - prev_odd
            if right == len(odds)-1:
                right_even = len(nums) - odds[right]
            else:
                right_even = odds[right+1] - odds[right]
                
            
            if right - left == k-1:
                total += left_even * right_even
                left += 1
            
        return total
        