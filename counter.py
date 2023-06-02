# Enter your code here. Read input from STDIN. Print output to STDOUT
s = int(input())
sizes = list(map(int, input().split()))
cus = int(input())
shoes = []
prices = []

for _ in range(cus):
    elem = input().split(" ")
    shoe = int(elem[0])
    price = int(elem[1])
    if shoe in sizes:
        shoes.append(int(shoe))
        sizes.remove(shoe)
        prices.append(int(price))
        
print(sum(prices))
