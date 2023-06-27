class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
#         for i in range(len(arr)):
#             to_right = arr[i+1:]
            
#             if len(to_right) < 1:
#                 continue
#             else:
#                 arr[i] = max(to_right)
                
#         arr[-1] = -1
        
#         return arr
                   
        max_elem = -1
        
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > max_elem:
                arr[i], max_elem = max_elem, arr[i]
            else:
                arr[i] = max_elem

        return arr


      """
      Time: O(N)
      Space: O(1)
      """
