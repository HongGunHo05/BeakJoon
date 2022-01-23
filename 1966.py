from collections import deque
import sys

# 3     3번 테스트 할 것

# 1 0       n = 1, m = 0
# 5         중요도 = 5

# 4 2           n = 4, m = 2
# 1 2 3 4       중요도 = 1 2 3 4

# 6 0               n = 6, m = 0
# 1 1 9 1 1 1       중요도 = 1 1 9 1 1 1

testcase = int(sys.stdin.readline())  # 테스트케이스 횟수 입력

for i in range(testcase):  # 테스트횟수 만큼 돌 때
    n, m = map(int, sys.stdin.readline().split())
    # n : 문서의 개수
    # m : 몇 번째로 인쇄 되었는지 궁금한 문서가 현재 큐에서 몇 번째에 놓여 있는지 나타 내는 정수

    queue = deque(map(int, sys.stdin.readline().split()))  # 중요도를 큐에 입력 받음
    indexqueue = deque([])  # 각 중요도가 몇번째 인덱스에 있는지 확인 할 큐

    count = 0  # 몇 번째에 빠져 나가야 하는지 알기 세기 위한 변수

    for j in range(n):  # 인덱스 위치를 큐에 넣어준다
        indexqueue.append(j)

    if n == 1:  # 문서의 개수가 1개이면 무조건 첫번째로 빠져 나간다
        print(count + 1)
        continue

    while True:
        if queue[0] != max(queue):  # 큐의 처음이 가장 큰 수가 아닐 경우
            queue.append(queue.popleft())  # 큐의 처음을 빼고 맨뒤로 보낸다
            indexqueue.append(indexqueue.popleft())  # 인덱스 큐도 처음을 빼고 맨뒤로 보낸다

        else:  # 큐의 처음이 가장 큰 수일 경우
            count += 1  # 빠져야 하기에 빠져 나가는 횟수 1 추가

            if indexqueue[0] == m:  # 만약 인덱스 큐의 처음이 몇 번째로 빠져 나가는지 알고 싶은 수라면
                break  # 멈춘다
            queue.popleft()  # 큐의 처음을 뺀다
            indexqueue.popleft()  # 인덱스 큐의 처음을 뺀다

    print(count)  # 결과 출력

