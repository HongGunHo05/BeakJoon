import sys

n = int(sys.stdin.readline())  # 사람 수 입력 받음

p = list(map(int, sys.stdin.readline().split()))  # 각각 걸리는 시간

p.sort()  # 최소 정리

sum = 0  # 각 사람마다 걸리는 시간
fi = 0  # 총 걸리는 시간

for i in p:
    sum += i
    fi += sum

print(fi)  # 결과 출력
