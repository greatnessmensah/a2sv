class DisjointSet:
    def __init__(self, size: int):
        self.root = {i: i for i in range(size)}
        self.size = [1] * size
        
    def find(self, node: int) -> int:
        root = node
        
        while root != self.root[root]:
            root = self.root[root]

        while node != root:
            parent = self.root[node]
            self.root[node] = root
            node = parent
            
        return root
    
    def union(self, u: int, v: int) -> None:
        rootV = self.find(v)
        rootU = self.find(u)
        
        if rootV != rootU:
            if self.size[rootV] > self.size[rootU]:
                self.root[rootU] = rootV
                self.size[rootV] += self.size[rootU]
            else:
                self.root[rootV] = rootU
                self.size[rootU] += self.size[rootV]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        df = DisjointSet(n)
        emails = {}
        
        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]

                if email not in emails:
                    emails[email] = i
                else:
                    df.union(i, emails[email])

        components = defaultdict(list)
        
        for email, group in emails.items():
            group_id = df.find(group)
            components[group_id].append(email)
            
        ans = []
        for group, emails in components.items():
            emails.sort()
            emails.insert(0, accounts[group][0])
            ans.append(emails)

        return ans
