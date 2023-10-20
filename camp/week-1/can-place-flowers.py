class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if flowerbed[0] == 0:
#             flowerbed.insert(0, 0)
#         else:
#             flowerbed.insert(0, 1)
            
#         if flowerbed[-1] == 0:
#             flowerbed.insert(len(flowerbed), 0)
#         else:
#             flowerbed.insert(len(flowerbed), 1)
            
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
        return n <= 0