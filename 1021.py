from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
#  큐의 크기, 뽑아내려고 하는 수의 개수 입력 받는다

outque = deque(map(int, sys.stdin.readline().split()))
#  뽑아내려고 하는 수를 입력 받는다

que = deque(i for i in range(1, n + 1))  # 큐의 크기 만큼 수를 채워 큐를 만든다
count = 0  # 몇번 연산을 수행 하는지 세는 변수

for i in outque:  # 뽑아내려고 하는 수를 하나씩 가져 온다
    while True:
        if i == que[0]:  # 뽑아내려고 하는 수와 큐의 첫 부분과 같으면
            que.popleft()  # 큐의 첫부분을 제거 시키고 멈추게 한다
            break

        if len(que) // 2 >= que.index(i):
            # 큐의 길이의 반 보다 큐에서 원하는 수의 위치가 작거가 같을 경우
            que.append(que.popleft())  # 큐의 맨 앞을 빼 맨 뒤로 보낸다
            count += 1
        else:  # 큐의 길이의 반 보다 큐에서 원하는 수의 위차가 클 경우
            que.appendleft(que.pop())  # 큐의 맨 뒤를 빼서 앞으로 가져온다
            count += 1

print(count) # 결과 출력



