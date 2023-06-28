n = int(input())
 
for i in range(n + 1):
    spaces = " " * (n - i) * 2
    digits = " ".join(str(j) for j in range(i))
 
    if i != 0:
        print(spaces + digits + " " + str(i) + " " + digits[::-1])
    else:
        print(spaces + str(i))
 
for i in range(n - 1, -1, -1):
    spaces = " " * (n - i) * 2
    digits = " ".join(str(j) for j in range(i))
 
    if i != 0:
        print(spaces + digits + " " + str(i) + " " + digits[::-1])
    else:
        print(spaces + str(i))


"""
Time: O(N^2)
Space: O(N^2)
"""
