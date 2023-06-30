def insertionSort1(n, arr):
    n = len(arr)
    for step in range(1, n):
        key = arr[step]
        j = step - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            print(*arr)
        arr[j + 1] = key
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

"""
Time: O(N^2)
Space: O(1)
"""
