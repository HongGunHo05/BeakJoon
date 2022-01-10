import sys


def move(n, f, s, t):
    if n >= 1:
        move(n - 1, f, t, s)

        print(f, t)

        move(n - 1, s, f, t)


n = int(sys.stdin.readline())

print(2 ** n - 1)

move(n, 1, 2, 3)

