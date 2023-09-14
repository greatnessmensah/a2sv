# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
#         l, r = 0, n-1
        
#         while l <= r:
#             mid = l + (r-l)//2
#             if isBadVersion(mid) == False:
#                 l = mid + 1
#             else:
#                 r = mid -1
                
#         return l


        left, right = 0, n-1
        best = n
    
        while left <= right:
            mid = left + (right-left) // 2
            if isBadVersion(mid):
                right = mid - 1
                best = mid
            else:
                left = mid + 1
                
        return best