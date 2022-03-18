import sys

strike = []
li = []

for i in range(123, 988):
    s = str(i)
    if "0" in s:
        continue
    elif s[0] != s[1] and s[0] != s[2] and s[1] != s[2]:
        li.append(list(s))
        strike.append(list(s))

for i in range(int(sys.stdin.readline())):
    guessnum, ansst, ansba = map(int, sys.stdin.readline().split())
    guessnum = str(guessnum)

    for num in strike:
        st = 0
        ba = 0
        lis = list(guessnum)

        for j in range(3):
            if num[j] == guessnum[j]:
                lis.remove(num[j])
                st += 1
        ba += len(set(lis) & set(num))

        if ansst == st and ansba == ba:
            continue
        else:
            if num in li:
                li.remove(num)
            else:
                pass
print(len(li))
