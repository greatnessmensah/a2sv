t = int(input())
 
for _ in range(t):
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
 
    if max(first) == max(second) and min(first) + min(second) == max(first):
        print("Yes")
    else:
        print("No")
