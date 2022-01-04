a, b, n = map(int, input().split())

li = []
i = 0

while i < n + 1:
    if a < b: # 분자가 분모보다 작을 경우
        a *= 10
        li.append(0)

    li.append(int(a/b)) # 나누고 몫을 리스트에 추가
    namuzi = int(a%b)
    a =namuzi * 10

    i += 1

print((li[n]))
