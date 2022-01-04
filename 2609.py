a, b = map(int, input().split())

num1 = []
mu1 = []
mu2 = []

for i in range(1, min(a, b) + 1): # 최대 공약수
    if (a % i == 0) and (b % i == 0):
        num1.append(i)

#최소 공배수
for i in range(1, b+1):
    mu1.append(i * a)

for i in range(1, a+1):
    mu2.append(i * b)

for i in mu1:
    if i in mu2:
        f = i
        break


print(max(num1)) # 최대 공약수
print(f) # 최소 공배수