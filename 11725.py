import sys
sys.setrecursionlimit(10**6)


def dfs(st):
    for i in graph[st]:
        if visit[i] == 0:
            visit[i] = st
            dfs(i)


n = int(sys.stdin.readline())

graph = list([] for _ in range(n+1))

visit = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2, n + 1):
    print(visit[i])
