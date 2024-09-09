class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @lru_cache
#         def dp(i, hi, wid):
#             if i >= len(books):
#                 return hi
            
#             w, h = books[i]
#             res = dp(i+1, h, w) + hi
            
#             if w + wid <= shelfWidth:
#                 return min(res, dp(i+1, max(hi, h), w+wid))
            
#             return res
        def dp(idx):
            if idx == len(books):
                return 0
            wi, hi = 0, 0
            ans = float('inf')
            
            for i in range(idx, len(books)):
                w, h = books[i]
                hi = max(hi, h)
                if w + wi <= shelfWidth:
                    ans = min(ans, hi+dp(i+1))
                wi += w 
            return ans
        
        return dp(0)
                
