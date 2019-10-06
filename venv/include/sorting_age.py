# https://www.acmicpc.net/problem/10814
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한
# # 순서대로 주어진다.
# # 이때, 회원들을 나이가 증가하는 순으로,
# # 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로
# # 정렬하는 프로그램을 작성하시오
#
# 3
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung
#
# 20 Sunyoung
# 21 Junkyu
# 21 Dohyun

n = int(input())
array = []
for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]),input_data[1]))
array = sorted(array,key=lambda x:x[0])
for i in array:
    print(i[0],i[1])

# (20,A) 나이순서 x[0] 로 정렬

