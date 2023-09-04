import math
 
 
def solve():
    n = int(input())
    left = 1
    right = round(math.pow(n, 1 / 3))
    found = False
     
    while (left <= right):
        curr = (left * left * left + right * right * right)
        if (curr == n):
            found = True
            break
        if (curr < n):
            left += 1
        else:
            right -= 1
     
    print("YES" if found else "NO")
 
t = int(input())
for _ in range(t):
    solve()
