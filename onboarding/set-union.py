# Enter your code here. Read input from STDIN. Print output to STDOUT
inp1 = int(input())
english = set(map(int, input().split()))

inp2 = int(input())
french = set(map(int, input().split()))

print(len(english.union(french)))
