t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
 
    maxv = max(nums)
    minv = min(nums)
    maxi = nums.index(maxv) + 1
    mini = nums.index(minv) + 1
 
    print(mini, maxi)

"""
Time: O(N)
Space: O(1)
"""
