import sys

w = []
for _ in range(int(sys.stdin.readline())):
    w.append(sys.stdin.readline().strip())

sw = set(w)
w = list(sw)
w.sort()
w.sort(key=len)

for i in w:
    print(i)



