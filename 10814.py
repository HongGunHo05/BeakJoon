import sys

li = []  # 회원 저장 하기 위한 리스트

for i in range(int(sys.stdin.readline())):  # 온라인 저지 회원의 수 입력 받고 그 만큼 돈다
    age, name = sys.stdin.readline().split()  # 나이와 이름을 입력 받는다
    li.append([int(age), name])  # 나이와 이름을 리스트에 저장한다

li.sort(key=lambda li:li[0])  # 람다를 이용해 나이를 기준으로 정렬한다

for i in li:  # 결과 출력한다
    print(i[0], i[1])