class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                t = stack.pop()
                temps[t[1]] = i - t[1]
            stack.append((temperatures[i], i))
            
        return temps
