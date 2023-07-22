def solve():
    s = input()
    ans = float('inf')
    n = len(s)
    res = []
 
    for x in s:
        if not res or res[-1][0] != x:
            res.append((x, 1))
        else:
            res[-1] = (res[-1][0], res[-1][1] + 1)
 
    m = len(res)
 
    for i in range(1, m - 1):
        if res[i - 1][0] != res[i + 1][0]:
            ans = min(ans, res[i][1] + 2)
 
    if ans > n:
        ans = 0
        
    print(ans)
 
 
t = int(input())
for _ in range(t):
    solve()
