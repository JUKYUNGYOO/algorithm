# 선택정렬
# 가장 작거나 큰 원소를 선택해서 가장 앞쪽으로 보냄

n = int(input())
array = list()
for _ in range(n):
    array.append(int(input()))

#i는 앞쪽에 위치한 인덱스
for i in range(n):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1,n):
        #가장 작은 원소와 보고있는 원소를 비교 
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index],array[i]
    #스와프
for i in array:
    print(i)
    #그 결과를 출력

# n = int(input())
# array = list()
# for _ in range(n):
#     array.append(int(input()))
# array.sort()
# for i in array:
#     print(i)
#











