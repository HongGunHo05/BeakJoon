import sys


def fix(a, b, i):
    """
    :param a: 물이 새는 곳 개수
    :param b: 테이프 길이
    :param i: 물이 새는 곳 위치가 있는 리스트
    :return: 테이프가 몇개가 필요 할까
    왼쪽에서 정수만큼 떨어진 거리만 물이 샌다.
    위치의 좌우 0.5 만큼 간격을 주어야 한다.
    """
    count = 1  # 총 필요한 테이프 개수
    start = i[0]  # 처음 시작 하는 위치

    if b == 1:  # 테이프 길이가 1이면
        return a  # 새는 위치 개수 리턴

    for j in i:  # 리스트 하나씩 가져 온다
        locate = start + b - 1  # 비교할 대상을 넣어준다
        # 시작 + 테이프 길이 - 1
        if j <= locate:  # 비교할 대상보다 같거나 작다면
            continue  # 그냥 넘어가고
        else:  # 크다면
            start = j  # 가져온 것을 시작위치에 넣어준다
            count += 1  # 테이프 개수 추가

    return count  # 테이프 개수 리턴


n, l = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

print(fix(n, l, li))