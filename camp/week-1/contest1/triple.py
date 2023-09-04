from collections import Counter
 
def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    maxi = -1
    count = 1
 
    for idx in range(1, n):
        if nums[idx-1] == nums[idx]:
            count += 1
        else:
            count = 1
        if count >= 3:
            maxi = max(maxi, nums[idx])
 
    print(maxi)
 
t = int(input())
for _ in range(t):
    solve()
