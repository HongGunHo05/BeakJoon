import sys

n, m = map(int, sys.stdin.readline().split())   # 자연수 n, 한 라인에 몇개 출력 할지 입력

li = []  # 스택을 위해 만듬


def dfs(st):
    if len(li) == m:  # 길이가 같으면
        print(" ".join(map(str, li)))  # 출력문 출력

    for i in range(st, n+1):  # 시작 하는 부분 부터 입력 받은 부분 + 1 까지 돌면서
        if i in li:  # i가 스택에 있다면 넘어감
            continue
        li.append(i)  # 없다면 스택에 추가
        dfs(i + 1)  # 재귀를 통해 다음 부터 갈 수 있게 호출
        li.pop()  # 끝난 후에는 빼내어서 다시 돌아오게 한다


dfs(1)  # 1부터 시작하기에 1 넣고 호출




