def solve():
    n = int(input())
    s = "#" + input() + "#"
    count = 0
    
    for i in range(1, len(s)-1):
        if s[i] == ".":
            count += 1
            if s[i-1] == "." and s[i+1] == ".":
                print(2)
                return
            
    print(count)

for _ in range(int(input())):
    solve()
