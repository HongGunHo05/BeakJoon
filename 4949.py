while True:
    n = input()
    # 문자열을 입력 받는다

    li = []  # 괄호들을 넣어줄 리스트

    if n == ".":  # 입력 받은 문자열이 . 이면
        break

    for i in n:  # 입력 받은 문자열들의 문자를 하나씩 가져온다
        if i == "(" or i == "[":  # ( 또는 [ 면
            li.append(i)  # 리스트에 추가 시킨다
        elif i == ")":  # ) 면
            if len(li) > 0 and li[-1] == "(":
                # 리스트 길이가 0보다 크고 끝이 ( 면 끝을 내보낸다
                li.pop()
            else:  # 위 조건이 아니면 추가 시키고 멈춘다
                li.append(i)
                break

        elif i == "]":
            # 리스트 길이가 0보다 크고 끝이 [ 면 끝을 내보낸다
            if len(li) > 0 and li[-1] == "[":
                li.pop()
            else:  # 위 조건이 아니면 추가 시키고 멈춘다
                li.append(i)
                break

    if len(li) == 0:  # 리스트 길이가 0이면 모두 짝이 맞다는 의미이다
        print("yes")  # 결과 출력
    else:
        print("no")

