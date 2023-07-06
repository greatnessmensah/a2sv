def solve():
    t = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = sorted(arr)
    
    if arr == sorted_arr:
        print("yes")
        print("1 1")
        return

    first_diff_index = -1
    last_diff_index = -1
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            first_diff_index = i
            break

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != sorted_arr[i]:
            last_diff_index = i
            break

    reversed_segment = arr[first_diff_index : last_diff_index + 1][::-1]
    updated_arr = arr[:first_diff_index] + reversed_segment + arr[last_diff_index + 1:]

    if updated_arr == sorted_arr:
        print("yes")
        print(first_diff_index + 1, last_diff_index + 1)
    else:
        print("no")

if "__main__" == __name__:
    solve()

"""
Time: O(N)
Space: O(N)
"""
