from collections import Counter
 
s = input()
counted = Counter(s)
if len(counted.keys()) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")

"""
Time: O(N)
Spce: O(N)
"""
