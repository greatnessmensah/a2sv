class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        queue = deque(["0000"])
        count = 0
        
        while queue:
            
            length = len(queue)
            for _ in range(length):
                key = queue.popleft()
                if key in visited:
                    continue
                visited.add(key)
                if key == target:
                    return count
                
                for i in range(4):
                    x = int(key[i])
                    for j in [-1, 1]:
                        num = key[:i] + str((x + j) % 10) + key[i+1:]
                    
                        if num not in visited:
                            queue.append(num)
                            
            count += 1
                            
        return -1
