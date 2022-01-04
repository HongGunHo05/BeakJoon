wb = ["WBWBWBWB", "BWBWBWBW"] * 4
bb = ["BWBWBWBW", "WBWBWBWB"] * 4
c = 32
y, x = map(int, input().split())
li = []

def cb(st):
    bc = 0
    wc = 0
    for i in range(len(st)):
        for j in range(len(st[i])):
            if st[i][j] != wb[i][j]:
                wc += 1
            if st[i][j] != bb[i][j]:
                bc += 1
    return min(wc, bc)

for i in range(y):
    li.append(input())

for i in range(y - 7):
   for j in range(x - 7):
       nl = li[i:i+8]
       for k in range(len(nl)):
           nl[k] = nl[k][j:j+8]
       c = min(c, cb(nl))

print(c)