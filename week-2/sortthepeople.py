class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        zipped = zip(names, heights)

#         for i in range(len(zipped)):
#             check = False
#             for j in range(len(zipped) - i - 1):
#                 if zipped[j][1] < zipped[j + 1][1]:
#                     zipped[j], zipped[j+1] = zipped[j+1], zipped[j]
#                     check = True
                    
#             if not check:
#                 break
            
#         return [pair[0] for pair in zipped]
			        
        for i in range(len(zipped)):
            min_idx = i
            for j in range(i + 1, len(zipped)):
                if zipped[min_idx][1] < zipped[j][1]:
                    min_idx = j
            zipped[i], zipped[min_idx] = zipped[min_idx], zipped[i]
                
        return [pair[0] for pair in zipped]


"""
Time: O(N^2)
Space: O(1)
"""
