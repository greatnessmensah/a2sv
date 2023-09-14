class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         left = 0
#         right = len(letters) - 1
        
#         while left <= right:
#             mid = (left + right) // 2
            
#             if letters[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
                
#         return letters[left % len(letters)]

#         alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#         chars = alpha[alpha.index(target)+1:]
        
#         i = 0
#         while i < len(chars):
#             left, right = 0, len(letters) - 1

#             while left <= right:
#                 mid = left + (right-left) // 2

#                 if letters[mid] > chars[i]:
#                     right = mid - 1
#                 elif letters[mid] < chars[i]:
#                     left = mid + 1
#                 else:
#                     return chars[i]
#             i += 1
#         return letters[0]

        left = 0
        right = len(letters) - 1
        nextt = letters[0]
        
        while left <= right:
            mid = (left + right) // 2
            
            if letters[mid] > target:
                right = mid - 1
                nextt = letters[mid]
            else:
                left = mid + 1
                
        return nextt