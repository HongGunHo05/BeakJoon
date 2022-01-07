n = int(input()) # 리스트 개수 지정
a = list(map(int, input().split())) # 첫번째 리스트 생성후 입력 받음
b = list(map(int, input().split())) # 두번째 리스트 생성후 입력 받음

a = sorted(a) # 오름차순으로 정렬
b = sorted(b, reverse = True) # 내림차순으로 정렬

sum = 0 # 총 합을 위해 생성

while n > 0:
    """
    while 문을 통해 
    a 리스트에서 가장 작은 것과 
    b 리스트에서 가장 큰것을 곱하게 한다
    """
    sum += a[n-1] * b[n-1]
    n -= 1

print(sum) # 결과 출력