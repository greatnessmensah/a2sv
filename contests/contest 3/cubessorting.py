t = int(input())

for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    
    found = False
    for i in range(1, n):
        if cubes[i] >= cubes[i-1]:
            found = True
            break
    
    if found:
        print("YES")
    else:
        print("NO")

"""
Time: O(N)
Space: O(1)
"""
