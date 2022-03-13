import sys

li = []
for i in range(int(sys.stdin.readline())):  # 입력 받은 수 만큼
    n = int(sys.stdin.readline())  # 숫자 입력
    li.append(n)  # 입력 받은 수를 리스트에 추가

l = set(li)  # 중복제거
li = list(l)  # 다시 리스트에 넣는다
li.sort()  # 정렬을 해준다

for i in li:  # 하나하나 받아 오면서
    print(i)  # 결과 출력