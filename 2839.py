import sys


def sugar(i):
    """
    :param i: 설탕 총 무게
    :return: 설탕 봉지 개수
    """
    sugarbag = 0  # 설탕 봉지 개수

    while i >= 0:  # 설탕 무게가 0 이상일 경우
        if i % 5 == 0:  # 설탕 무게가 5로 나뉘어 떨어지면
            sugarbag += i // 5  # 5로 나눈 몫을 봉지 개수에 추가
            return sugarbag  # 총 설탕 봉지 개수 리턴

        i -= 3  # 설탕 무게에서 3씩 뺀다
        sugarbag += 1  # 봉지 개수를 하나씩 추가 시킨다


n = int(sys.stdin.readline())  # 설탕 총 무게 입력 받음

if sugar(n) is None:  # 함수 호출 결과가 없으면
    print(-1)  # -1 출력
else:  # 함수 호출 결과가 있으면
    print(sugar(n))  # 결과 출력
