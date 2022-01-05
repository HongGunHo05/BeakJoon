n = int(input())
dsnb = [[0,1] , [-1,0], [0,-1], [1,0]] #북 서 남 동

for i in range(n):
    turtle = [0, 0]  # 현재 위치
    turn = 0 # 회전
    mn = [0, 0] # 최솟값 좌표
    mx = [0, 0] # 최댓값 좌표

    move = input()

    for j in move:
        if j == "F": # 전진
            turtle[0] += dsnb[turn][0]
            turtle[1] += dsnb[turn][1]

        elif j == "B": # 후진
            turtle[0] -= dsnb[turn][0]
            turtle[1] -= dsnb[turn][1]

        elif j == "L": # 왼쪽으로 회전
            if turn == 3:
                turn = 0
            else:
                turn += 1

        elif j == "R": # 오른쪽으로 회전
            if turn == -3:
                turn = 0
            else:
                turn -= 1

        if mn[0] > turtle[0]: # 죄소 좌표, 최대 좌표 구하기
            mn[0] = turtle[0]
        elif mx[0] < turtle[0]:
            mx[0] = turtle[0]

        if mn[1] > turtle[1]:
            mn[1] = turtle[1]
        elif mx[1] < turtle[1]:
            mx[1] = turtle[1]

    print((mx[0] - mn[0]) * (mx[1] - mn[1]))