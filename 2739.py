# 구구단 출력
n = int(input()) # 출력할 구구단 단수 입력 받기
for i in range(1,10): # 1에서 9단까지 반복문 돌기
    print("%d * %d = %d"%(n, i, n*i)) # 출력