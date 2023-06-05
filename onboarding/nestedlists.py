from collections import defaultdict


records = []
hashmap = defaultdict(list)

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([score, name])
        
    for record in records:
        key, value = record
        hashmap[key].append(value)
    
    hashmap = dict(sorted(hashmap.items(), key= lambda x : x[0]))
    
    names = list(hashmap.values())[1]
    names.sort()
    
    print("\n".join(names))
    
    # for name in names:
    #     print(name)
