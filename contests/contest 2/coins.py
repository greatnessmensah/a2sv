t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    found = False
 
    for x in range(2):
        if n - x * k >= 0 and (n - x * k) % 2 == 0:
            print("YES")
            found = True
            break
 
    if not found:
        print("NO")

"""
Time: O(1)
Space: O(1)
"""
