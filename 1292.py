import sys

a, b = map(int, sys.stdin.readline().split())  # 구간의 시작, 끝을 입력 받는다
que = []  # 구간을 넣어 주기 위한 리스트

for i in range(100):  # 100까지 돌 때
    for j in range(i):  # i 번 만큼 i를 큐에 넣는다
        que.append(i)
print(sum(que[a-1:b]))  # 구간에서 시작부터 끝까지의 합을 출력 한다
