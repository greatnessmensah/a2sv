def solve():
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    diffs = []
 
    for i in range(n):
        diffs.append(arr1[i]-arr2[i])
 
    diffs.sort()
    l, r = 0, n-1
    count = 0
 
    while l < r:
        if diffs[l] + diffs[r] <= 0:
            l += 1    
        else:
            count += (r-l)
            r -= 1
 
    print(count)
 
 
if "__main__" == __name__:
    solve()
