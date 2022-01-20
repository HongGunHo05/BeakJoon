import sys
import math  # 제곱근을 사용하기 위해


def solution(num):
    """
    :param num: 수를 하나 받아 온다
    :return: 아래 조건에 따라 참인지 거짓인지 리턴한다
    """
    if num == 1:  # 1이면 바로 거짓으로 리턴한다
        return False

    for j in range(2, int(math.sqrt(num)) + 1):  # 2부터 제곱근까지 하나하나 늘리면서
        if num % j == 0:  # 받아온 수에 나누어 0으로 떨어지면
            return False  # 거짓으로 리턴
    return True  # 위 조건에 하나도 부합 하지 않으면 참으로 리턴


n, m = map(int, sys.stdin.readline().split())
# 자연수 두개를 받는다

for i in range(n, m+1):  # 자연수 두개 사이의 수를 하나하나 가져 온다
    if solution(i):  # 각 수에 따라 함수 호출하고 참이면
        print(i)  # 결과 출력



