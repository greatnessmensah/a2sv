def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    l = 0
    count = 0
    
    for idx, num in enumerate(nums):
        while l < n and nums[l] - nums[idx] <= 5:
            l += 1
            count = max(count, l-idx)
           
    print(count)

if "__main__" == __name__:
    solve()
