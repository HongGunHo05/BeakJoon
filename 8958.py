n = int(input())
li = []

for i in range(n):
    s = 0
    c = 0
    li.append(input())
    for a in li[i]:
        if a == "o" or a == "O":
            c+=1
        else:
            c = 0
        s += c
    print(s)