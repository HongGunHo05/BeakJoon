import sys


def check(st):
    for i in range(st):
        if line[st] == line[i] or abs(line[st] - line[i]) == st - i:
            return False
    return True


def dfs(st):
    global count

    if st == n:
        count += 1
    else:
        for i in range(n):
            line[st] = i
            if check(st):
                dfs(st + 1)


n = int(sys.stdin.readline())   # 자연수 n 입력

line = [0] * n  # 몇번째 줄에 몇번째 칸에 있는지 알기 위해 만듬
global count
count = 0

dfs(0)

print(count)