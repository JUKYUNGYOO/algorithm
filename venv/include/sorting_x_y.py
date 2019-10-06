# https://www.acmicpc.net/problem/11650
#
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3
#
# 2차원 평면 위의 점 N개가 주어진다.
# 좌표를 x좌표가 증가하는 순으로,
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한
# 다음 출력하는 프로그램을 작성하시오.
#
# 1.(x좌표,y좌표)를 입력 받은 뒤, x좌표, y좌표
# 순서대로 차례대로 오름차순 정렬
# 2. 파이썬의 기본 정렬 라이브러리는 기본적으로 튜플의
# 인덱스 순서대로 오름차순 정렬
# 3. 따라서 단순히 기본 정렬 라이브러리를 이용하면
# 됩니다. (key 속성 설정 없이)

n = int(input())
array = []
for _ in range(n):
    x,y = map(int, input().split(' '))
    array.append((x,y))
array = sorted(array)
for i in array:
    print(i[0],i[1])