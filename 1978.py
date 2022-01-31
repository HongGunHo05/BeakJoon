import sys


def sq(num):
    i = 2

    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))

count = 0

for i in li:
    if i == 1:
        continue
    if sq(i):
        count += 1

print(count)
