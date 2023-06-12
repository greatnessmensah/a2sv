t = int(input())

for _ in range(t):
    input()
    res = []
    hashmap = {}
    sol = []
    for i in range(8):
        value = list(input()) # [.....#..]
        res.append(value)
        
        hashmap[i] = value.count("#")
        
    for i in range(1, 7):
        if hashmap[i] == 1 and hashmap[i-1] == 2 and hashmap[i+1] == 2:
            sol.append(i)

    row_containing_bishop = res[sol[0]]

    for i in range(len(row_containing_bishop)):
        if row_containing_bishop[i] == "#":
            sol.append(i)


    print(sol[0]+1, sol[1]+1)
        
