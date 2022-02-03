import sys

n, k = map(int, sys.stdin.readline().split())

count = 0

li = []

for i in range(n):
    li.append(int(sys.stdin.readline()))

for i in range(n-1, -1, -1):
    count += k // li[i]
    k = k % li[i]
print(count)





