t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = a[0]

    for i in range(n-2):
        b[i+1] = min(a[i], a[i+1])
    
    b[-1] = a[-1]

    print(*b)
