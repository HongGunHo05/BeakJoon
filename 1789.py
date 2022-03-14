import sys

s = int(sys.stdin.readline())  # 자연수의 합 입력

sum = 0  # 총 합을 구하기 위해 만듬

i = 1  # 1부터 하나하나 올림
count = 0  # 개수 센다

while(True):
    if i > s - sum:  # 만약 자연수 합 - 총 합이 i 보다 작으면
        break  # 반복문 멈춘다
    else:  # 만약 자연수 합 - 총 합이 i 보다 크면
        count += 1  # 하나씩 개수 올리면서
        sum += i  # 총 합에 i를 더해준다.
        i += 1  # i 1씩 올린다
        # 마지막 수는 마지막 i에서 더해줘야 하는 값을 더한 수이기 때문에 추가로 더해 줄 필요 없다
print(count)  # 결과 출력
