N = int(input())  # 단어 수 입력
li = []  # 단어들을 넣어줄 리스트 생성
m = ("", 0)  # 최대값 넣어 주기 위해 생성
for i in range(N):  # 입력한 수 만큼 단어 입력
    ti = input()
    li.append(ti)  # 리스트에 추가

hi = {}  # 딕셔너리 생성
for i in li:  # 리스트를 돈다
    hi[i] = hi.get(i, 0) + 1
    # get(단어,0)을 하여 처음 보는 단어가 나오면 0 리턴 해주고 1 더해준 뒤
    # 딕셔너리에 넣어준다
hi = sorted(hi.items())  # 딕셔너리를 sorted로 정렬한다

for i in hi:  # 딕셔너리를 돈다
    if i[1] > m[1]:  # 최대값보다 크면
        m = i  # i를 최대값에 넣어준다

print(m[0])  # 결과 출력