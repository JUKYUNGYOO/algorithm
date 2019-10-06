#https://www.acmicpc.net/problem/2798
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한
#가까운 3장의 합을 구해 출력

n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))
result =0
length = len(data)
count = 0

for i in range(0,length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)
                #sum 값과 result를 비교해서 가장 큰 값을
                # result에 넣어줌
print(result)












