t = int(input())
words = []
for _ in range(t):
    phrase = (input().split(" "))
    sorted_phrase = sorted(phrase, key=lambda x: int(''.join(char for char in x if char.isdigit())))

    filtered_words = [''.join([char for char in word if not char.isdigit()]) for word in sorted_phrase]

    print(" ".join(filtered_words))
                 