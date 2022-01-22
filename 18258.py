from collections import deque  # 큐를 사용하기 위해 만듬
import sys

n = int(sys.stdin.readline())  # 입력 받을 명령어 개수
queue = deque([])  # 큐를 사용하기 위해 만듬

for i in range(n):  # 명령어 개수 만큼 돌 때
    commend = sys.stdin.readline().split()  # 명령어 입력 받음
    if commend[0] == "push":  # push를 할 때
        queue.append(commend[1])  # 입력 받은 정수를 큐에 넣어준다

    elif commend[0] == "pop":  # pop을 할 때
        if len(queue) != 0:  # 큐 길이가 0이 아니라면
            print(queue.popleft())  # 큐 맨 앞쪽을 pop하고 출력한다
        else:  # 길이가 0이라면
            print(-1)  # -1 출력

    elif commend[0] == "size":  # size를 할 때
        print(len(queue))  # 큐 길이를 출력한다

    elif commend[0] == "empty":  # empty를 할 때
        if len(queue) == 0:  # 큐 길이가 0이라면
            print(1)  # 1을 출력
        else:  # 큐 길이가 0이 아니라면
            print(0)  # 0 출력

    elif commend[0] == "front":  # front를 할 때
        if len(queue) != 0:  # 큐 길이가 0이 아니라면
            print(queue[0])  # 큐 맨 앞을 출력
        else:  # 큐 길이가 0이라면
            print(-1)  # -1 출력

    elif commend[0] == "back":  # back을 할 때
        if len(queue) != 0:  # 큐 길이가 0이 아니라면
            print(queue[-1])  # 큐 맨 뒤를 출력
        else:  # 큐 길이가 0이라면
            print(-1)  # -1 출력

