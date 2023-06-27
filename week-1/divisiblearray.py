t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = []
    for i in range(1, n+1):
        nums.append(i*2)
 
    print(*nums)
