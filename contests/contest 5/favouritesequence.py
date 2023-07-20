def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    res = []
    l, r = 0, n-1
 
    while l <= r:
        res.append(nums[l])
        res.append(nums[r])
        l += 1
        r -= 1
 
    if n == 1:
        print(*nums)
    else:
        print(*res[:n])
 
t = int(input())
for _ in range(t):
    solve()


"""
Time: O(N)
Space: O(N)
"""
