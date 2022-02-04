import sys

n = int(sys.stdin.readline())  # 정수 하나 입력 받는다

count = 0  # 몇번 나오는지 세기 위한 변수

num = "666"  # 666이 들어가면 세기 위해 만듬
i = 666  # 숫자를 돌리기 위해 만듬

while count < n:  # 원하는 만큼 세기
    if num in str(i):  # 666이 들어간 숫자가 있다면
        count += 1  # count에 1을 더함
    i += 1  # 숫자를 1씩 올림

print(i - 1)  # 결과 출력









