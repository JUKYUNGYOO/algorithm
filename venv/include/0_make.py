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

n = int(input())
for i in range(n):
    m = int(input())


