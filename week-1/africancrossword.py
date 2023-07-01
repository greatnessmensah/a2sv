n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
res=''
for i in range(n):
    for j in range(m):
        ans = 0
        for k in range(m):
            if grid[i][j] == grid[i][k]:
                ans += 1
        for l in range(n):
            if grid[i][j] == grid[l][j]:
                ans += 1
        if ans == 2:
            res += grid[i][j]
 
print(res)

"""
Time: O(N*M(N+M)
Space: O(N*M)
"""
