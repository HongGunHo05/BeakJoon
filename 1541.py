import sys
"""
- 를 기준으로 생각을 해야 최소가 된다
"""
w = sys.stdin.readline().split("-")  # - 를 빼고 리스트로 만든다
w[len(w) - 1] = w[len(w) - 1][:-1]  # 맨 마지막 인덱스에서 /n을 뺀다

li = []  # 마지막 총 계산을 구하기 위해 리스트 만듬
for i in w:  # 하나하나 받아오면서
    if "+" not in i:  # + 가 없으면
       li.append(int(i))  # 바로 리스트에 저장

    else:
        i = i.split("+")  # + 를 기준으로 숫자들을 리스트로 만들어 저장
        s = 0  # 합을 위해 만듬
        for j in i:  # 하나하나 가져 오면서
            s += int(j)  # 숫자로 만들어 더해준다
        li.append(s)  # 총 합을 리스트에 저장

sum = li[0]  # 처음 숫자를 총 합에 넣는다.
for i in range(1, len(li)):  # 1부터 시작하여 리스트 총 크기 전까지 돌면서
    sum -= li[i]  # 총 합에서 뺴준다.

print(sum)  # 결과 출력