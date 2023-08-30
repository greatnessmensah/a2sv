class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        suffix = [0] * len(shifts)
        suffix[-1] = shifts[-1]
        i = len(shifts)-2
        res = ""
        
        while i > -1:
            suffix[i] = suffix[i+1] + shifts[i]
            i -= 1
            
        for i in range(len(suffix)):
            res += chr((ord(s[i])- ord('a')+suffix[i])%26+97)
            
        return res
               