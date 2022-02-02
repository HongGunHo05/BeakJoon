import sys

li = []  # 소수들이 들어갈 리스트

for i in range(2, 10000):  # 2 부터 1만 까지 돌면서
    if i % 2 != 0:  # 2로 나누었을 때 나머지가 1인 것들을
        li.append(i)  # 리스트에 넣는다

for i in range(3, 100, 2):  # 3부터 시작해서 100까지 (1만의 루트는 백이라서) 2씩 더하며 돌면서
    for j in range(i * 2, li[-1] + 1, i):  # 홀수의 2배부터 리스트를 돌면서 홀수의 배수가 있다면
        if j in li:  # 리스트에서 제거 시킨다
            li.remove(j)
li.insert(0, 2)  # 처음 소수의 시작은 2라 추가 시킨다

for _ in range(int(sys.stdin.readline())):  # 테스트 개수를 입력 하여 돌린다
    n = int(sys.stdin.readline())  # 원하는 짝수를 입력하여
    half = n // 2  # 짝수의 반을 구해
    for i in range(half, 1, -1):
        # 반부터 점점 1씩 1까지 작아지게 돌면서 (두 수의 차가 제일 작은 것을 구하기 위해)
        if n - i in li and i in li:
            # 만약 반부터 시작한 수가 소수리스트에 있고 입력받은 짝수에 빼고 난 뒤의 수도 리스트에 있다면
            print(i, n - i)  # 결과 출력한다
            break
