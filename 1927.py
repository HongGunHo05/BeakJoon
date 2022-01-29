import sys, heapq

n = int(sys.stdin.readline())  # 연산의 개수 입력

heap = []  # 힙을 하나 만든다

for i in range(n):  # 연산의 개수만큼 돈다
    a = int(sys.stdin.readline())  # 정수 입력

    if a != 0:  # 0이 아니라면
        heapq.heappush(heap, (a, a))  # 힙에 튜플 형식으로 추가 한다
    else:  # 0이라면
        if len(heap) == 0:  # 힙이 길이가 0이면
            print(0)  # 0 출력
        else:  # 0이 아니라면
            print(heapq.heappop(heap)[1])  # 힙에서 튜플 형식의 인덱스 1을 제거 하며 출력 한다
