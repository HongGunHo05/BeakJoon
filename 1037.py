import sys

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))
li.sort()

print(li[0] * li[-1])









