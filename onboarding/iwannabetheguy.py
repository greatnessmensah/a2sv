t = int(input())
 
 
x = list(map(int, input().split()))
y = list(map(int, input().split()))
 
 
levels = set(x[1:] + y[1:])
 
if len(levels) >= t:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
