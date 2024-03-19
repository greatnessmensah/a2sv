def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    perm = [n+1-nums[i] for i in range(n)]

    print(*perm)

for _ in range(int(input())):
    solve()
