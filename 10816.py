import sys
from collections import Counter

n = int(sys.stdin.readline())
nnum = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
mnum = list(map(int, sys.stdin.readline().split()))

count = Counter(nnum)

for i in mnum:
    if i not in count:
        print(0, end=" ")
    else:
        print(count[i], end=" ")
