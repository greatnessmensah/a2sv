def solve():
    t = int(input())
 
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        found = False
 
        for i in range(n):
            if a[i] != b[i] and a[i] + 1 != b[i]:
                print("NO")
                found = True
                break
        
        if not found:
            print("YES")
 
if "__main__" == __name__:
    solve()
