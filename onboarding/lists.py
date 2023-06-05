if __name__ == '__main__':
    N = int(input())
    inp = list()
    for _ in range(N):
        s=input().strip().split(" ")
        if s[0]=="insert":
            inp.insert(int(s[1]),int(s[2]))
        if s[0]=="print":
            print(inp)
        if s[0]=="remove":
            inp.remove(int(s[1]))
        if s[0]=="append":
            inp.append(int(s[1]))
        if s[0]=="sort":
            inp.sort()
        if s[0]=="pop":
            inp.pop()
        if s[0]=="reverse":
            inp.reverse()
