def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    l, r = 0, n-1
    sums = 0
 
    while l < r:
        sums += (nums[r] - nums[l])
        l += 1
        r -= 1
 
    print(sums)
 
 
t = int(input())
for _ in range(t):
    solve()
