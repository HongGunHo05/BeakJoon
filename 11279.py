import sys, heapq  # 힙을 쓰기 위해 사용

n = int(sys.stdin.readline())  # 연산의 개수 입력 받음
heap = []  # 힙을 하나 만듬

for i in range(n):  # 연산의 개수 만큼 돌 때
    a = int(sys.stdin.readline())  # 정수 하나 입력 받음

    if a != 0:  # 입력 받은 정수가 0이 아니면
        heapq.heappush(heap, (-a, a))
        # 힙에다 튜플 형식으로 넣는다
        # 최대 힙이므로 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성 되는 원리 이용

    else:  # 0이면
        if len(heap) == 0:  # 힙 길이가 0이면
            print(0)  # 0 출력
        else:  # 길이가 0이 아니라면
            print(heapq.heappop(heap)[1])  # 힙 인덱스 1 부분을 잘라 출력 한다
