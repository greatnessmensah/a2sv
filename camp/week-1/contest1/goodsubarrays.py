from collections import defaultdict
 
 
def solve():
    n = int(input())
    s = list(input())
    nums = [int(i) for i in s]
    window = defaultdict(int)
    window[0] = 1
    curr = ans = 0
 
    for right in range(n):
        curr += nums[right]-1
        ans += window[curr]
        window[curr] += 1
 
    print(ans)
 
t = int(input())
for _ in range(t):
    solve()
