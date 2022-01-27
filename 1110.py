import sys

n = int(sys.stdin.readline())  # 정수 하나 입력 받는다
a = n  # a 라는 변수에 n을 넣는다

count = 0  # 몇번만에 돌아 왔는지 카운트

while True:
    a = a % 10 * 10 + (a // 10 + a % 10) % 10
    # 일의 자리 뺀 것을 10 곱하고
    # (십의 자리 + 일의 자리)를 10으로 나누고 나머지를 더한다
    count += 1  # 카운트 + 1

    if a == n:  # 만약 같아 졌다면 멈춘다
        break

print(count)  # 결과 출력


