def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        s_nums = sorted(nums)
        diffs = []
 
        for i in range(n):
            if nums[i] == s_nums[-1]:
                diff = nums[i] - s_nums[-2]
                diffs.append(diff)
            else:
                diff = nums[i] - s_nums[-1]
                diffs.append(diff)
 
        print(*diffs)
 
 
 
if "__main__" == __name__:
    solve()

"""
Time: O(NlogN)
Space: O(N)
"""
