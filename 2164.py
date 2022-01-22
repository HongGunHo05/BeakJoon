from collections import deque  # 큐를 사용하기 위해 만듬
import sys

n = int(sys.stdin.readline())  # 카드 수를 입력
queue = deque([])  # 큐를 위해 만듬

for i in range(1, n+1):  # 카드마다 번호를 넣어 준다
    queue.append(i)

while True:
    if len(queue) == 1:  # 큐 길이가 1이면 멈춘다
        break

    queue.popleft()  # 큐 맨앞을 제거 시킨다
    queue.append(queue.popleft())  # 큐 맨 앞을 제거 하면서 맨 뒤에 저장 시킨다


print(queue[0])  # 결과 출력
