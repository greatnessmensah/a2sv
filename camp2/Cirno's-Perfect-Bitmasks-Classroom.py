def solve():
    n = int(input())

    if n == 1:
        print(3)
        return
    num = 0

    for i in range(33):
        if n & (1 << i):
            num += (2 ** i)
            if num != n:
                break
            else:
                num += 1
                break
    print(num)

for _ in range(int(input())):
    solve()
