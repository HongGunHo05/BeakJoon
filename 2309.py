li = []

for i in range(9):  # 9개를 입력 받음
    li.append(int(input()))

li.sort()  # 리스트 정렬

sum_li = sum(li)  # 리스트 총합을 저장

fir = 0
sec = 0

for i in range(8):  # 하나를 지정하고
    for j in range(i + 1, 9):  # 지정한 수 다음 부터 돌게 한다
        if sum_li - (li[i] + li[j]) == 100:  # 총합 - 지정 두수 = 100 이면
            fir = li[i]  # 각 변수에 저장
            sec = li[j]

# 리스트에서 값을 제외시킨다
li.remove(fir)
li.remove(sec)

# 리스트를 돌며 결과 출력
for i in li:
    print(i)