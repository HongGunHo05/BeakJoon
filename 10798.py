li = []
a = []
for i in range(5):
    li.append(input())
    a.append(len(li[i]))

mx = max(a)

st = ""
i = 0
j = 0

while j < mx:
    while i < 5:
        if j < a[i]:
            st += li[i][j]  #
        i += 1
    i = 0
    j += 1

print(st)