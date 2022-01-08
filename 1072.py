import sys

a, b = map(int, sys.stdin.readline().split()) # 두 수 입력 받음
z = int(100 * b / a) # 처음 게임을 돌리기 전 승률

if z >= 99: # 확률이 99프로가 넘어가면 바뀌지 않으니 바로 결과 출력
    print(-1)
else:
    r = a  # 추가 할 수 있는 범위 중 제일 큰 값
    l = 0  # 추가 할 수 있는 범위 중 제일 작은 값

    choiso = a # 게임 수를 최대로 잡아 놓음

    while l <= r: # 범위의 큰 부분이 작은 범위보가 작을 경우 멈춤
        m = (l + r) // 2 # 추가 할 수 있는 범위 중 중앙 값

        if z < (100 * (b + m) // (a + m)):
            # 중앙값을 넣어 확률 구하고 비교 후 처음 승률 보다 클 경우
            choiso = m # 중앙 값을 저장
            r = m - 1 # 범위 큰 부분을 줄임
        else:
            l = m + 1 # 처음 승률보다 작을 경우 범위 왼쪽 부분을 키움

    print(choiso) # 결과 출력