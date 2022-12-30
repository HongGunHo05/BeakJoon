import sys

n = int(sys.stdin.readline())

arr = set(sys.stdin.readline().split())

m = int(sys.stdin.readline())

for i in sys.stdin.readline().split():
    if i in arr:
        print(1, end=" ")
    else:
        print(0, end=" ")