def solve():
    s = str(input())
    res = set()
    l = 0
 
    while l < len(s):
        if l+1 >= len(s) or s[l] != s[l+1]:
            res.add(s[l])
            l += 1
        else:
            l += 2
    
    print("".join(sorted(list(res))))
 
 
t = int(input())
for _ in range(t):
    solve()
