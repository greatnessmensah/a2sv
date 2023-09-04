def solve():
    t = int(input())
    nums = list(map(int, input().split()))
    n = int(input())
    ns = list(map(int, input().split()))
    nums.sort(reverse=True)
    summ = sum(nums)
    
    for n in ns:
        print(summ - nums[n-1])
          
if "__main__" == __name__:
    solve()
