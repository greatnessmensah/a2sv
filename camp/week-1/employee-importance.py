"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashmap = {emp.id: emp for emp in employees}
        count = 0
        
        def dfs(idx):
            nonlocal count
            for sub in hashmap[idx].subordinates:
                count += hashmap[sub].importance
                dfs(sub)
                
        dfs(id)
        
        return count + hashmap[id].importance
        
