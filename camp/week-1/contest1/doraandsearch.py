def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    left = 0
    right = n-1
    mini = 1
    maxi = n
 
    while left < right:
        if nums[left] == maxi or nums[right] == maxi:
            if nums[left] == maxi:
                left += 1
            else:
                right -= 1
            maxi -= 1
        elif nums[left] == mini or nums[right] == mini:
            if nums[right] == mini:
                right -= 1
            else:
                left += 1
            mini += 1
        else:
            print(left+1,right+1)
            return
 
    print(-1)
 
t= int(input())
for _ in range(t):
    solve()
