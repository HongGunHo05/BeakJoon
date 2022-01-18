import sys

n = int(sys.stdin.readline())  # 스택에 들어갈 숫자 개수

stack = []  # 스택을 리스트로 구현
final = ""  # 결과 + - 를 넣기 위한 변수
mx = 0  # 비교하기 위한 대상

for i in range(n):  # 숫자 개수 만큼 돌 때
    num = int(sys.stdin.readline())  # 숫자 입력

    if mx < num:
        # 전에 입력 했던 가장 큰 수 보다 이번에 입력 한 수가 더 크다면
        j = num - mx
        # 전에 입력 된 가장 큰수와 차이를 구해 사이에 개수가 몇개 있는지 파악하기 위해 만든 변수
        while True:
            stack.append(num-(j-1))
            # 만약 mx가 4 이고 num이 6일시에 5, 6을 넣어야 하니까 이전 수부터 넣어 준다
            j -= 1
            final += "+"  # 스택에 넣어 줄 때마다 + 를 결과변수에 넣어준다
            if j == 0:  # 사이의 수가 없기에 j가 0이 된다면 멈춘다
                break
        mx = num  # 입력 받은 수가 최대 이므로 비교 대상에 넣어준다
        stack.pop()  # 끝에 있는 수를 제거 한다
        final += "-"  # 결과 변수에 -를 넣어준다

    elif mx > num:
        # 전에 입력 했던 가장 큰 수 보다 이번에 입력 한 수가 더 작다면
        if stack[-1] == num:  # 스택의 끝에 있는 수와 입력 받은 수와 같다면
            stack.pop()  # 끝 수를 제거 한다
            final += "-"  # 결과 변수에 - 를 추가한다
        else:  # 다르다면 수열이 성립이 되지 않으므로
            final = "NO"  # 결과변수를 NO로 만들고 멈춘다
            break

# 각 결과 변수에 맞는 조건문에 들어가 결과 출력
if final == "NO":
    print(final)
else:
    for i in final:
       print(i)
