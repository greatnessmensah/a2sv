t = int(input())
 
def power_of_two(x):
    cur = 1
 
    while cur <= x:
        cur *= 2
 
    return cur
 
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(n)
    for i in range(1, n+1):
        print(i, power_of_two(a[i-1]) - a[i-1])
