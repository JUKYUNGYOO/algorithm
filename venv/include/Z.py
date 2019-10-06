# https://www.acmicpc.net/problem/1074

def solve(n,x,y):
    global result
    # 현재 함수의 크기가 2*2 일때만 종료조건을 만듬 
    if n== 2:
        if x==X and y==Y:
            print(result)
            return
        result += 1
        if x==X and y+1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y+1 == Y:
            print(result)
            return
        result += 1
        return
    solve(n/2,x,y)
    solve(n/2,x,y+n/2)
    solve(n/2,x+n/2,y)
    solve(n/2,x+n/2,y+n/2)
result = 0
N,X,Y = map(int,input().split(' '))
solve(2 ** N,0,0)
#처름 입력을 받았을 때, 2^N을 크기로 입력받