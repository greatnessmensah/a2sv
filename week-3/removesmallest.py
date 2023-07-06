def solve():
    t = int(input())
 
    for _ in range(t):
        n = int(input())
        nums = list(map(int, (input().split())))
        nums.sort()
        found = True
 
        for i in range(n):
            if (nums[i] - nums[i-1]) > 1:
                print("NO")
                found = False
                break
 
        if found:
            print("YES")
 
if "__main__" == __name__:
    solve()
