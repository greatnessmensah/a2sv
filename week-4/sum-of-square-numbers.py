class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = [i for i in range(int(pow(c,0.5))+1)]
        l, r = 0, len(nums)-1
        
        while l <= r:
            if nums[l]**2 + nums[r]**2 == c:
                return True
            elif nums[l]**2 + nums[r]**2 < c:
                l += 1
            else:
                r -= 1
            
        return False
        