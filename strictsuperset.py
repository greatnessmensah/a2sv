# Enter your code here. Read input from STDIN. Print output to STDOUT
hashset = set(map(int, input().split()))

t = int(input())
bools = []

for _ in range(t):
    childset = set(map(int, input().split()))
    
    if hashset.intersection(childset) == childset:
        bools.append(True)
    else:
        bools.append(False)
        
if sum(bools) == len(bools):
    print(True)
else:
    print(False)
