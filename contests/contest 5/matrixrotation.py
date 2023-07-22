def solve():
    nums = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    nums += arr
    maxi = nums.index(max(nums))
    mini = nums.index(min(nums))

    if maxi+mini == 3:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()
