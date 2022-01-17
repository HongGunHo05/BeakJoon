import sys


def bracket(w):
    """
    :param w: 입력한 괄호 문자열
    :return: 각 입력한 괄호에 대한 응답
    """
    count = 0  # 괄호에 따라 연산을 해주기 위한 변수

    if w[-1] == "(":  # 끝이 "(" 면 닫히지 않는 것이니 바로 NO 출력
        return "NO"

    for j in w:  # 괄호 문자열을 하나씩 받아와
        if j == "(":  # "("면
            count += 1  # count에 1을 더해준다
        elif j == ")":  # ")"면
            count -= 1  # count에 1을 빼준다
        if count < 0:
            # count가 0 밑으로 내려가면 닫히는 괄호가 앞에 더 있다는 것 이므로 바로 NO 출력
            return "NO"

    if count == 0:  # count가 0 이면 짝에 맞게 괄호가 있다는 것이다
        return "YES"
    else:  # 여기서 else는 count가 0보다 클 경우로 열리는 괄호가 더 있다는 것이다
        return "NO"

    count = 0  # count를 다시 0으로 초기화 시킨다


t = int(sys.stdin.readline())  # t개의 테스트 데이터 개수 입력

for i in range(t):  # t개 만큼 돌때
    w = sys.stdin.readline()  # 괄호로 이루어진 문자열 입력
    print(bracket(w))  # 함수 호출
