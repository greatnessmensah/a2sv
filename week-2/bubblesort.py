def countSwaps(a):
    numSwaps = 0
    for i in range(len(a)):
        swapped = False
        for j in range(0, len(a)-i-1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numSwaps+=1
        swapped = True

        if not swapped:
            break
    
    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
  

"""
Time: O(N^2)
Space: O(1)
"""
