def solve():
    n = input()
    n = n.split(" ")
    char = n[1]
    s = input()
    s += s
    maxi = 0
    count = 0
    i = 0
    while i < len(s):
        if s[i] == char:
            count = 0
            while i < len(s) and s[i] != 'g':
                count += 1
                i += 1
            if count > maxi:
                maxi = count
        i += 1
    print(maxi)
 
t = int(input())
for _ in range(t):
    solve()
