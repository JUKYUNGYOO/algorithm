# https://www.acmicpc.net/problem/7490

# 0 만들기
# 1부터 N까지의 수를 오름차순으로 쓴 수열 1,2,3,...N을
# 생각하자
# 그리고 +,-,또는 공백을 숫자 사이에 삽입
# 이렇게 만든 수식의 값을 계산하고
# 그 결과가 0이 될 수 있는지를 살피자
#
# 첫번째 줄에 테스트 케이스의 개수가 주어진다
# 각 테스트 케이스엔 자연수 N이 주어진다
#
# 2
# 3
# 7
# 1. 자연수 N의 범위(3<=N<=9) 가 매우 한정적 이므로
# 완전 탐색으로 문제를 해결 할 수 있다.
# 수의 리스트와 연산자 리스트를 분리하여 모든 경우의 수를 계산
# 가능한 모든 경우를 고려하여 연산자 리스트를 만듬.(재귀 함수 이용)
# 파이썬의 eval() 함수를 이용하여 문자열 형태의 표현식 계산

import copy
def recursive(array,n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return
    array.append('')
    recursive(array,n)
    array.pop()

    array.append('+')
    recursive(array,n)
    array.pop()

    array.append('-')
    recursive(array,n)
    array.pop()

test_case = int(input())
for _ in range(test_case):
    operators_list = []
    n = int(input())
    recursive([],n-1)


    integers = [i for i in range(1,n+1)]

    for operators in operators_list:
        string = ""
        for i in range(n-1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(" ","")) == 0:
            print(string)
    print()


