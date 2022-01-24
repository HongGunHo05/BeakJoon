from collections import deque
import sys

n = int(sys.stdin.readline())  # 명령어 개수 입력 받는다
que = deque([])  # 덱을 만든다

for i in range(n):  # 명령어 개수 만큼 돌 때
    commend = sys.stdin.readline().split()  # 명령어 입력 받는다

    # 각각에 맞는 명령어 실행한다
    if commend[0] == "push_front":
        que.appendleft(commend[1])

    elif commend[0] == "push_back":
        que.append(commend[1])

    elif commend[0] == "pop_front":
        if len(que) != 0:
            print(que.popleft())
        else:
            print(-1)

    elif commend[0] == "pop_back":
        if len(que) != 0:
            print(que.pop())
        else:
            print(-1)

    elif commend[0] == "size":
        print(len(que))

    elif commend[0] == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)

    elif commend[0] == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])

    elif commend[0] == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])



