# Enter your code here. Read input from STDIN. Print output to STDOUT
value = input().split()
sub = int(value[0])
stu = int(value[1])

scores = []
for _ in range(stu):
    marks = list(map(float, input().split()))
    scores += [marks]
    
zipped = zip(*scores)

for item in zipped:
    summed = sum(item)
    avg = summed / stu
    print(avg)
