t = int(input())

for _ in range(t):
    word = str(input())

    two_letters = "".join(word[:2])
    
    print(f"{two_letters}... {word}?")