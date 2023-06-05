# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

num = int(input())
hashmap = OrderedDict()

for _ in range(num):
    value = input().split(" ")
    item_name = " ".join(value[:-1])
    price = int(value[-1])
        
    
    if item_name not in hashmap:
        hashmap[item_name] = price
    else:
        hashmap[item_name] += price
    
for key, value in hashmap.items():
    print(key, value)
