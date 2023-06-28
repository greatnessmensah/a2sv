from statistics import mean
 
t = int(input())
nums = list(map(int, input().split()))
m = mean(nums)
means = 0
indices = []
 
for num in range(len(nums)):
    if nums[num] == m:
        means += 1
        indices.append(num+1)
 
print(means)
print(*indices)

"""
Time: O(N)
Space: O(N)
"""
