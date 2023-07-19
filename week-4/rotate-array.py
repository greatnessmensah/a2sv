class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        we set k to be the mod of len(nums)
        we reverse from l, r, l to k and k to r.
        """
        k = k % len(nums)
        l, r = 0, len(nums)-1
        
        def reverse(start,end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        reverse(l, r)
        reverse(l, k-1)
        reverse(k, r)

    
    """
    Time: O(N)
    Space: O(1)
    """