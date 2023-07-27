def solve():
    """
    check if current element is greater than previous then we set rise to True
    if a sequence is rising and the current is lesser than previous 
    set found to False.
    """
    n = int(input())
    nums = list(map(int, input().split()))
    rise = False
    found = True
 
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            rise = True
        if nums[i] < nums[i-1] and rise:
            found = False
 
    if found:
        print("YES")
    else:
        print("NO")
 
 
t = int(input())
for _ in range(t):
    solve()
