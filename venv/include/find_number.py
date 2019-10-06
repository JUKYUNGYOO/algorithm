

# 주어진 정수안에 특정 정수가 존재하는지?
# https://www.acmicpc.net/problem/1920
# 첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다.
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1≤M≤100,000)이 주어진다.
# 다음 줄에는 M개의 수들이 주어지는데,
# 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수들의 범위는 int 로 한다.

# 5 (N)
# 4 1 5 2 3 N개의 정수 (A)
# 5 (M)
# 1 3 7 9 5 M개의 정수
#  M개의수들이 A안에 존재하는가?

# 1
# 1
# 0
# 0
# 1

# 5개입력
n = int(input())
array = set(map(int,input().split()))
m = int(input())
x = list(map(int,input().split()))
for i in x:
    if i not in array:
        print('0')
    else:
        print('1')


# set 집합 - 중복을 허용하지 않음
# 특정 정수의 등장 여부만을 간단히 체크
# Python에서는 dictionary 자료형을 해시처럼 사용
# 본 문제는 set자료형을 이용해 더욱 간단히 풀 수 있다

# set으로 바꾸게 되면
# [3,5,7] -> {3,5,7}

