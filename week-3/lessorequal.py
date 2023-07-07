def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
 
    arr.sort()
    ans = None
    count = 0
 
    if k == 0:
        ans = arr[0] - 1
    else:
        ans = arr[k-1]
 
    for i in range(n):
        if ans >= arr[i]:
            count += 1
 
    if ans < 1 or count != k:
        print(-1)
    else:
        print(ans)
 
if "__main__" == __name__:
    solve()
