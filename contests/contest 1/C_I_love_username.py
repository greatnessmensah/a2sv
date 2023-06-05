t = int(input())

marks = list(map(int, input().split()))
min_mark = max_mark = marks[0]
count = 0

for mark in marks:
    if mark > max_mark:
        max_mark = mark
        count += 1
    elif mark < min_mark:
        min_mark = mark
        count += 1

print(count)

