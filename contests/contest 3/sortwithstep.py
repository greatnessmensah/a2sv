def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in range(0, n):
        nums[i] -= 1

    bad = 0
    for i in range(0, n):
        if nums[i] % k != i % k:
            bad += 1

    if bad == 0:
        print(0)
    elif bad == 2:
        print(1)
    else:
        print(-1)


t = int(input())
for _ in range(t):
    solve()

"""
Time: O(N)
Space: O(1)
"""
