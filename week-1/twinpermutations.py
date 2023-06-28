t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    perm = [n+1-nums[i] for i in range(n)]
 
    print(*perm)
