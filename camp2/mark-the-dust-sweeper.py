def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    flag = False
    zeroes = 0
    count = 0

    for i in range(n-1):
        if nums[i] != 0:
            count += nums[i]
            flag = True
        else:
            if flag:
                zeroes += 1

    print(count+zeroes) 

for _ in range(int(input())):
    solve()
