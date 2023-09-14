class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        occurrences = []

#         while left <= right:
#             mid = (left + right) // 2
#             if arr[mid] == target:
#                 occurrences.append(mid)
                
#                 back = mid - 1
#                 while back >= left and arr[back] == target:
#                     occurrences.append(back)
#                     back -= 1
                    
#                 forward = mid + 1
#                 while forward <= right and arr[forward] == target:
#                     occurrences.append(forward)
#                     forward += 1

#                 return [min(occurrences), max(occurrences)] if len(occurrences) > 1 else occurrences + occurrences
#             elif arr[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

        left, right = 0, len(arr)-1
        best = -1
        
        while left <= right:
            mid = left + (right-left) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid -1
            else:
                right = mid -1
                best = mid
       
        occurrences.append(best)
        
        left, right = 0, len(arr)-1
        best = -1
        
        while left <= right:
            mid = left + (right-left) // 2
            if arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                left = mid + 1
                best = mid

        occurrences.append(best)
        
        return occurrences