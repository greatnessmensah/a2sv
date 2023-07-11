def solve():
    t= int(input())
 
    for _in in range(t):
        n, c = map(int, input().split())
        nums = list(map(int, input().split()))
        ans = 0
        hashmap = {}
 
        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
            if hashmap[nums[i]] <= c:
                ans += 1
 
        print(ans)
 
if "__main__" == __name__:
    solve()

"""
Time: O(N)
Space: O(N)
"""
