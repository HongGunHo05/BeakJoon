import sys


def game(l):
    """
    :param i: 레벨의 수
    :param l: 각 레벨에서 얻는 점수 리스트
    :return: 점수를 내려야 하는 횟수
    """
    count = 0  # 점수를 내려야 하는 횟수
    locate = len(l) - 1  # 끝부터 돌리기 위해 위치를 지정 하려고 만든 변수
    while 0 < locate:  # 위치가 0 보다 크다면 반복
        if l[locate] <= l[locate - 1]:  # 리스트에서 원하는 위치와 원하는 위치의 전 것과 비교
            l[locate - 1] -= 1  # 전 것을 - 1 해준다
            count += 1  # 횟수에 + 1 해준다
            continue  # 반복문 다시 돌게 한다
        locate -= 1  # 비교후 원하는 위치의 수가 더 크다면 - 1 을 해줌과 동시에 위치 이동
    return count


n = int(sys.stdin.readline())  # 레벨의 수

li = []  # 게임 점수 리스트를 생성
for i in range(n):  # 게임 점수 리스트에 각 레벨마다 점수 입력
    li.append(int(sys.stdin.readline()))

print(game(li))  # 결과 출력
