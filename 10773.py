import sys

k = int(sys.stdin.readline())  # 앞으로 입력할 수의 수

stack = []  # 스택을 리스트로 표현

for i in range(k):  # k번 돌 때
    n = int(sys.stdin.readline())  # 수를 입력 받는다

    if n == 0:  # 입력 받은 수가 0이면
        stack.pop()  # 스택 맨 뒤를 제거시킨다
    else:  # 0이 아니면
        stack.append(n)  # 입력 받은 수를 스택 맨 뒤에 추가 시킨다

print(sum(stack))  # 스택의 총 합을 출력한다