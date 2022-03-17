import sys

s = sys.stdin.readline()  # 문자열을 하나 받아온다

zero = s.split("0")  # 0으로 구분해 배열로 저장
one = s.split("1")  # 1로 구분해 배열로 저장

if s[-2] == "0":  # \n 제거 작업
    zero = zero[:-1]
else:
    one = one[:-1]

z1 = zero.count("")  # 각각 배열에서 "" 부분을 세준다
o1 = one.count("")

if len(zero) - z1 < len(one) - o1:  # 총 길이에서 ""를 센 것을 빼주고 비교한다
    print(len(zero) - z1)  # 결과 출력
else:
    print(len(one) - o1)
