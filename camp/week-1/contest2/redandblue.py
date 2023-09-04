def solve():
    n = int(input())
    nums1 = list(map(int, input().split()))
    m = int(input())
    nums2 = list(map(int, input().split()))
    pref1 = [0] * (n+1)
    pref2 = [0] * (m+1)
 
    for i in range(n):
        pref1[i+1] = pref1[i] + nums1[i]
 
    for i in range(m):
        pref2[i+1] = pref2[i] + nums2[i]
 
    print(max(pref1)+max(pref2))
 
t = int(input())
for _ in range(t):
    solve()
