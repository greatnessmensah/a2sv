def solve():
    s = input()
    q = int(input())
    prefix = [0]
    count = 0
 
    for i in range(len(s)):
        if s[i] == s[i-1]:
            count += 1
            prefix.append(count)
        else:
            prefix.append(count)
            
    for i in range(q):
        x, y = map(int, input().split())
        print(prefix[y]-prefix[x])
 
if "__main__" == __name__:
    solve()
