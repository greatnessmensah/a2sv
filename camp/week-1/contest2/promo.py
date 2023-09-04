def solve():
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    prefix = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + nums[i-1]
    print(prefix)

    for _ in range(q):
        x, y = map(int, input().split())
        print(prefix[n-x+y],prefix[n-x])
    

if __name__ == '__main__':
    solve()
