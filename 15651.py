import sys

n, m = map(int, sys.stdin.readline().split())  # 자연수 n, 한 라인에 몇개 출력 할지 입력

li = []  # 스택을 위해 만듬


def dfs():
    if len(li) == m:  # 길이가 같으면
        print(" ".join(map(str, li)))  # 출력문 출력
        return

    for i in range(1, n + 1):  # 1부터 n까지 돌면서
        li.append(i)  # 리스트에 추가한다 중복은 생각 안해도 되니 if 문을 통해 빼지 않아도 된다
        dfs()  # 재귀를 통해 추가로 돌린다
        li.pop()  # 끝난 후에는 빼내어서 다시 돌아오게 한다


dfs()  # 함수를 호춣한다

