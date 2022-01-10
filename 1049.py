import sys

n, m = map(int, sys.stdin.readline().split())
# 끊어진 기타줄의 개수: n 기타줄 브랜드: m

sl, ol = [], []  # 패키지 값 리스트, 낱개 값 리스트
money = 0  # 총 가격

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    sl.append(a)
    ol.append(b)

a = min(sl)  # 패키지 값 중 최소값
b = min(ol)  # 낱개 값 중 최소값

if a < b * 6:  # 패키지를 구매 해야 하는 경우
    pn = n // 6  # 패키지 구매 개수
    money = pn * a  # 총합에 패키지 갯수 * 패키지 최소 가격을 한다
    n -= pn * 6  # 총 사야할 줄 수에서 줄을 산 수를 뺀다

if n >= 6:  # 패키지를 하나도 사지 않았을 경우
    money = b * n  # 낱개 최솟값으로 줄을 전부 산다
else:  # 패키지를 사고 나머지 줄을 사야 하는 경우
    if a < n * b:  # 나머지 줄 * 낱개 최솟값이 패키지의 최소 값보다 클 경우
        money += a  # 총합에 패키지의 값을 더해 준다

    else:  # 나머지 줄 * 낱개 최솟값이 패키지의 최소 값보다 작을 경우
        money += n * b  # 총합에 낱개 최솟값 * 나머지 줄 수의 값을 더해 준다

print(money)  # 총합을 출력한다
