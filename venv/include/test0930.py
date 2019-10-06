# https://www.acmicpc.net/problem/2920
#  음계
a = list(map(int, input().split(' ')))
# 입력 받은 정수 공백을 기준으로 나뉘어짐, map 을 이용해서 각각의 원소를 int로 바꾸어줌
ascending = True
descending = True

for i in range(1, 8):
    if a[i] > a[i - 1]:
        descending = False
    # a[2] > a[1] 오름차순 이므로, descending = False
    elif a[i] < a[i - 1]:
        ascending = False
if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')



