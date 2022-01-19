import sys


def solution(k):
    """
    :param k: 찾아야 될 수
    :return:  찾았으면 1, 못 찾았으면 NONE 리턴
    """
    low = 0  # 이분 탐색을 할 때 나눈 범위에서 제일 작은 쪽
    high = len(a) - 1  # 이분 탐색을 할 때 나눈 범위에서 제일 큰 쪽

    while high >= low:  # 높은 쪽이 낮은 쪽보다 커야됨
        mid = int((high + low) / 2)  # 범위의 중간 값을 구한다

        if a[mid] == k:  # 범위의 중간 값과 원하는 수와 같으면 찾았다는 의미 이므로
            return 1  # 결과 값 출력

        elif a[mid] > k:  # 범위의 중간 값이 원하는 수보다 더 크다면
            high = mid - 1
            # 범위의 큰 쪽을 중간값 - 1 을 하여 반으로 정하여 범위를 줄인다

        elif a[mid] < k:  # 범위의 중간 값이 원하는 수보다 더 크다면
            low = mid + 1
            # 범위의 큰 쪽을 중간값 - 1 을 하여 반으로 정하여 범위를 줄인다


n = int(sys.stdin.readline())  # 찾을 수가 있는지 확인 할 리스트 인덱스 개수

a = list(map(int, sys.stdin.readline().split()))  # 찾을 수가 있는지 확인 할 리스트
a.sort()  # 이분 탐색을 위한 리스트 정렬

m = int(sys.stdin.readline())  # 찾을 수를 넣어줄 리스트 인덱스 개수

b = list(map(int, sys.stdin.readline().split()))  # 찾을 수를 넣어줄 리스트

for i in range(m):  # 찾을 수를 넣어줄 리스트 인덱스 개수 만큼 돌 때
    if solution(b[i]) == 1:  # 함수를 호출 하고 리턴 값이 1 이면
        print(1)  # 1 출력
    else:  # 호출값이 1이 아니면
        print(0)  # 0 출력





