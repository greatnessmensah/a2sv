class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        nums.append(float('-inf'))
        b_index = -1
    
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                b_index = mid
                break
            elif nums[mid] < nums[mid+1] and nums[mid] > nums[mid-1]:
                lo = mid + 1
            else:
                hi = mid - 1
        
            
        return b_index