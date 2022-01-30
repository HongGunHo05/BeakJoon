import sys, heapq

hp = []

for _ in range(int(sys.stdin.readline())):  # 연산의 개수 입력 받고 그 만큼 돌 때
    x = int(sys.stdin.readline())  # 정수 입력 받는다

    if x != 0:  # 정수가 0이 아니라면
        heapq.heappush(hp, (abs(x), x))  # 힙에 튜플 형식으로 절대값 기준으로 추가 한다

    else:  # 0이라면
        if len(hp) == 0:  # 힙 길이가 0이라면
            print(0)  # 0 출력

        else:  # 길이가 0이 아니라면
            print(heapq.heappop(hp)[1])  # 맨 앞 튜플을 제거 하며 결과 출력 한다

