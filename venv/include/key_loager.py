# https://www.acmicpc.net/problem/5397

# 1) 스택 두 개를 만들고, 스택 두개의 중간 지점을 커서로 간주
# 2) 문자입력 : 왼쪽 스택에 원소 삽입
# 3) - 입력 : 왼쪽 스택에서 원소 삭제
# 4)< 입력 : 왼쪽 스택에서 오른쪽 스택으로 원소이동
# 5)> 입력: 오른쪽 스택에서 왼쪽 스택으로 원소이동
# 커서를 두 스택에 중간에 둔다고 가정

test_case = int(input())
for _ in range(test_case):
    left_stack =[]
    right_stack = []
    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
            elif i == '<':
                if left_stack:
                    right_stack.append(left_stack.pop())
            elif i == '>':
                if right_stack:
                    left_stack.append(right_stack.pop())
            else:
                left_stack.append(i)
                #단순하게 문자가 들어왔으면 left_stack에 넣어주면 됨
            left_stack.extend(reversed(right_stack))
            #right_stack 함수를 뒤집어서
            #left_stack에 붙여줌
            print(''.join(left_stack))