def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    mini = 1

    for i in range(n):
        if nums[i] <= mini:
            mini += nums[i]
        else:
            break

    print(mini)
    
if "__main__" == __name__:
    solve()
