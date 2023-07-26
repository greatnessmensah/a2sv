def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    subs = 0
    neg = False
 
    for num in nums:
        count += abs(num)
 
        if num < 0 and not neg:
            subs += 1
            neg = True
        elif num > 0:
            neg = False
 
    print(count, subs)
 
t = int(input())
for _ in range(t):
    solve()
