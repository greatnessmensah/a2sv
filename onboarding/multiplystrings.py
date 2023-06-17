class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = []
        rev = num2[::-1]
        
        for x in range(len(rev)):
            res = int(rev[x]) * int(num1) * (10 ** x)
            ans.append(res)

        
        return str(sum(ans))
      
      """
      Time: O(N)
      Space: O(N)
      """
        
        
