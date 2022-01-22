from collections import deque  # 큐를 사용하기 위해 만듬
import sys

n, k = map(int, sys.stdin.readline().split())  # 사람수, 제거 해야 할 순서 수 입력

queue = deque([])

for i in range(1, n + 1):  # 큐에 사람 수 만큼 숫자 넣어 준다
    queue.append(i)

print("<", end="")
while True:
    for i in range(k - 1):  # 제거 해야 할 수 바로 앞까지 돌면서
        queue.append(queue.popleft())  # 앞에 수를 뒤로 넘겨 준다

    print(queue.popleft(), end="")  # 순서가 되면 제거 하면서 출력 한다
    if len(queue) > 0:  # 출력문 형식에 맞게 출력 하기 위해 만듬
        print(",", end=" ")
    else:  # 길이가 0이 되면 멈추게 한다
        break
print(">")
