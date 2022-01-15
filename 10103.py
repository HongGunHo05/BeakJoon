import sys

n = int(sys.stdin.readline())  # 게임 수

player1, player2 = 100, 100  # 각 플레이어의 처음 점수

for i in range(n):  # 게임 수 만큼 게임을 함
    a, b = map(int, sys.stdin.readline().split())  # 매 라운드 마다 주사위 점수 입력
    if a > b:  # 플레이어 점수 비교
        player2 -= a  # 진 곳에 이긴 플레이어의 주사위 수를 뺸다
    elif a < b:
        player1 -= b

print(player1, player2)  # 결과 출력