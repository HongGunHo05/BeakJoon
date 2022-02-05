import sys

count = 0

for i in range(1,  int(sys.stdin.readline()) + 1):  # 정수 하나 입력 받고 그 만큼 돌린다
    if i == 1000:  # 입력 받은 수가 1000이면 넘어간다
        continue

    if i < 100:  # 100 미만 수는 모두 한수이다
        count += 1

    else:  # 100이 넘어가는 수이면
        if int(str(i)[2]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[0]):
            #  백의 자리와 십의 자리의 차와 십의 자리와 일의 자리 차가 같으면
            count += 1

print(count)  # 결과 출력

