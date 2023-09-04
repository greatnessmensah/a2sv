def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p = [0]
 
    for i in range(n):
        p.append(p[-1] + (a[i] if b[i] == 0 else 0))
 
    hours = 0 
 
    for i in range(k, len(p)):
        hours = max(hours, p[i]-p[i-k])
        
    print(sum([a[i] for i in range(n) if b[i]==1]) + hours)
 
if "__main__" == __name__:
    solve()
