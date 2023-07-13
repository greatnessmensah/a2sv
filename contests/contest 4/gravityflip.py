def solve():
    t = int(input())
    nums = list(map(int, input().split()))
 
    print(*list(sorted(nums)))
 
if "__main__" == __name__:
    solve()
