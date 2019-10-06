# 프린터 큐
# https://www.acmicpc.net/problem/1966
# 현재 리스트에서 가장 큰 수가 앞에
# 올 때 까지 회전시킨 뒤에 추출
# 가장 큰 수가 M이면서 가장 앞에 있을 때
# 프로그램 종료
#
# 나머지 문서들 중 현재 문서보다 중요도가
# 높은 문서가 하나라도 있다면,
# 이 문서를 인쇄하지 않고 큐의
# 가장 뒤에 재배치 한다.
#
# index =2
# count =0 #출력된 문서의 갯수
# 1 2 3 4
# m=2이므로 3번째 문서를 봄
#
# index=2
# count=0
# 가장큰수 =3
# 가장 큰 중요도를 가지는 문서가
# 앞에 올 때까지 회전
# 1 2 3 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3
# 가장 큰 수가 앞에 올 때 원소를 뽑음
# 4를 뽑음
# index =2
# count =1
# 가장큰수 =3
# 1 2 3
# 2 3 1
# 3 1 2
# 3을 뽑음
# count=2가 됨
# 목표로 하는 M이 2번째로 추출되었으므로
# 정답은 2
# index=2
# count=2
# 1 2
#
# test case에 대해서
# 문서의 수 N,몇번째로 인쇄 되었는지 알고싶은 원소

test_case = int(input())
for _ in range(test_case):
    n, m = list(map(int,input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    # idx를 튜플의 두번째 원소로 설정
    #[(2,0),(1,1),(4,2),(3,3)]
    # key = lambda x: x[0] 0번째 원소를 key로 사용
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x:x[0])[0]:
            count += 1
            if queue[0][1] == m:
                 print(count)
                 break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
# 프린터 큐
# https://www.acmicpc.net/problem/1966
# 현재 리스트에서 가장 큰 수가 앞에
# 올 때 까지 회전시킨 뒤에 추출
# 가장 큰 수가 M이면서 가장 앞에 있을 때
# 프로그램 종료
#
# 나머지 문서들 중 현재 문서보다 중요도가
# 높은 문서가 하나라도 있다면,
# 이 문서를 인쇄하지 않고 큐의
# 가장 뒤에 재배치 한다.
#
# index =2
# count =0 #출력된 문서의 갯수
# 1 2 3 4
# m=2이므로 3번째 문서를 봄
#
# index=2
# count=0
# 가장큰수 =3
# 가장 큰 중요도를 가지는 문서가
# 앞에 올 때까지 회전
# 1 2 3 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3
# 가장 큰 수가 앞에 올 때 원소를 뽑음
# 4를 뽑음
# index =2
# count =1
# 가장큰수 =3
# 1 2 3
# 2 3 1
# 3 1 2
# 3을 뽑음
# count=2가 됨
# 목표로 하는 M이 2번째로 추출되었으므로
# 정답은 2
# index=2
# count=2
# 1 2
#
# test case에 대해서
# 문서의 수 N,몇번째로 인쇄 되었는지 알고싶은 원소
#
# test_case = int(input())
# for _ in range(test_case):
#     n,m = list(map(int,input().split(' ')))
#     //4 2
#     queue = list(map(int, input().split(' ')))
#     //2 1 4 3
#     queue = [(i,idx) for idx, i in enumerate(queue)]
#     //enumerate
#     //특정한 튜플을 index와 같이 파악
#    //index를 튜플의 2번째 원소로 파악
#    //[2,1,4,3]
#    //[(2,0),(1,1),(4,2),(3,3)]
#     count = 0
#     while True: //무한 반복
#     //큐의 가장 앞쪽의 원소를 파악해서
#     //중요도가 가장 큰 것이 앞쪽에 있다면
#     //count증가
#     //맨 앞 원소가
#     //큐에서의 가장 큰 중요도와 일치한다면
#     //큐의 맨 앞쪽의 원소 == 큐의 가장 큰 원소
#     //queue[0][0] 큐의 맨 앞 쪽의 원소의, 중요도
#         if queue[0][0] == max(queue, key=lambda x:x[0])[0]:
#       //max(queue,key=lambda x:x[0])
#       큐에서의 가장 큰 중요도
#             count += 1
#             if queue[0][1] == m:
#             //뽑은 문서가 우리가 찾고자하는 m이라면
#                 print(count)
#                 //현재까지 몇번의 원소가 출력되는지
#                 break
#             else:
#                 queue.pop(0)
#                 //m이 아니라면 해당 문서를 뽑음
#         else:
#             queue.append(queue.pop(0))
#             //문서를 pop해서 뒤쪽으로 넣어줌
# //중요도가 높은 문서가 아니라면
# //문서를 뒤쪽으로 보냄