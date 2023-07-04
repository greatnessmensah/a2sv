t = int(input())

for _ in range(t):
    a, b, c = (map(int, input().split()))
    ans = []
    nom = abs(a-b) + abs(a-c) + abs(b-c)
    ans.append(nom)
    ax = [a-1, a, a+1]
    bx = [b-1, b, b+1]
    cx = [c-1, c, c+1]

    for i in range(len(ax)):
        for j in range(len(bx)):
            for k in range(len(cx)):
                abso = abs(ax[i] - bx[j]) + abs(ax[i] - cx[k]) + abs(bx[j] - cx[k])
                ans.append(abso)

    print(min(ans))

"""
Time: O(1)
Space: O(1)
"""
