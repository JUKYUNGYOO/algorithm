
# 파이썬 에서 데이터의 개수가 많을 때는
# sys.stdin.readline() 사용
# 빠름

import sys
n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1
    #인덱스에 해당하는 배열의 값을 1 증가
for i in range[10001]:
    if array[i] != 0:
        for j in range(array[i]):
            print(i)