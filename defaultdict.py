# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = input().split()

group_a = []
group_b = []

for _ in range(int(n)):
    group_a.append(input())
    
for _ in range(int(m)):
    group_b.append(input())

positions = defaultdict(list)

for i, word in enumerate(group_a):
    positions[word].append(i + 1)

for word in group_b:
    if word in positions:
        print(" ".join(str(pos) for pos in positions[word]))
    else:
        print("-1")
