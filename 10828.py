import sys

n = int(sys.stdin.readline())  # 명령어 수
stack = []  # 스택을 리스트로 표현

for i in range(n):  # 명령어 수 만큼 반복
    commend = sys.stdin.readline().split()  # 명령어 입력 받음
    if commend[0] == "push":  # push 할 때
        stack.append(commend[1])  # 같이 입력 받은 수를 맨 뒤에 넣어 준다
    elif commend[0] == "pop":  # pop 할 때
        if len(stack) == 0:  # 스택이 비워져 있다면
            print(-1)  # -1 출력
        else:  # 비워져 있지 않다면
            print(stack.pop())  # 스택 맨 뒤 삭제 후 삭제한 것 출력
    elif commend[0] == "top":  # top 할 때
        if len(stack) == 0:  # 스택이 비워져 있다면 
            print(-1)  # -1 출력
        else:  # 스택이 비워져 있지 않다면
            print(stack[len(stack) - 1])  # 스택 맨 뒤에 있는 것 출력
    elif commend[0] == "size":  # size 할 때
        print(len(stack))  # 스택의 길이 출력
    elif commend[0] == "empty":  # empty를 할 때
        if len(stack) == 0:  # 스택이 비워져 있다면
            print(1)  # 1 출력
        else:  # 비워져 있지 않다면 
            print(0)  # 0 출력


