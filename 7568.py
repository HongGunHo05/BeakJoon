import sys

li = []  # 입력 받은 키와 몸무게를 저장 하기 위해 만듬

for i in range(int(sys.stdin.readline())):  # 입력 받은 수 만큼 돌림
    li.append(list(map(int, sys.stdin.readline().split())))  # 키와 몸무게 입력 받음

for i in li:  # 하나하나 넣으면서 돌림
    rank = 1  # 랭크를 정하기 위해 만듬
    for j in li:  # 비교 하기 위해 하나 하나 넣음
        if i[0] < j[0] and i[1] < j[1]:  # 키랑 몸무게를 비교 한다 둘다 작으면 랭크 + 1
            rank += 1
    print(rank)  # 결과 출력

