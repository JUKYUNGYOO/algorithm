# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1
# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에
# 한 개씩 출력한다.
# push연산은 +로, pop 연산은 -로 표현하도록 한다.
# 불가능한 경우 NO를 출력한다.

n = int(input()) #8
count =1
stack =[]
result =[]
for i in range(1,n+1): #데이터 개수만큼 반복
    data = int(input())
    #데이터를 한줄에 하나씩 입력 받음
    #count가 1부터 n까지 증가하면서
    #스택에 넣어줌
    # 4를 출력하기 위해선 1부터 4까지 스택에 넣고
    # 4가 최상위 원소에 올라왔을 때 pop()

    while count <= data:  # data = 4
        #입력 받은 데이터에 도달할 때까지 삽입
        stack.append(count) # 1,2,3,4 삽입
        count +=1
        result.append('+')
        #삽입이 될때마다 result에 '+'를 담음
    if stack[-1] == data:
        #스택의 최상위 원소가 데이터와 같을 때 출력
        stack.pop()
        result.append('-')
    else: #불가능한경우

        print('No')
        exit(0)
print('\n',join(result)) #가능한 경우

#4를 출력하기 위해서 1부터4까지 스택에 넣어야됨
#4가 최상위에 올라와 있도록 만듬
#특정한 수에 도달할 때까지 데이터를 스택에 넣는다
#원소를 뽑을 때는
# join( list ) : 리스트에서 문자열으로