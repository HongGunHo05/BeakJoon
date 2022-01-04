n = int(input())
re = 1
c = 0

for i in range(1, n+1): # 팩토리얼 구하기
    re *= i

re = str(re)[::-1] # 숫자를 뒤집고 문자열로 넣는다

for i in re: # 0이 아니면 멈춘다
    if i != "0":
        break
    c+=1 # 0의 갯수 센다

print(c) # 결과 출력