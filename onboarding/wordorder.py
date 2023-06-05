# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

t = int(input())
hashmap = OrderedDict()

for _ in range(t):
    word = input()
    hashmap[word] = hashmap.get(word, 0) + 1
    
print(len(hashmap.keys()))
print(" ".join(str(x) for x in hashmap.values()))
