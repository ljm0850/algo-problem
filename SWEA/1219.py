import sys
sys.stdin=open('input.txt')

#한개의 정점에서 선택할 수 있는 길의 수 최대 2개, 정점은 최대 98개(시작,끝점 제외), 시작점은 0 끝점은 99
def tour(s):
    visit[s] = 1
    stack = [s]
    while True:
        if s == end:
            return 1
        visit[s] = 1
        for i in way[s]:
            if visit[i] == 0:
                s = i
                stack.append(s)
                break
        else:
            stack.pop()
            if not stack:
                return 0
            else:
                s = stack[-1]

for _ in range(10):
    tc,N = map(int,input().split())             # tc = 테스트케이스, N = 길의 총 개수
    target = list(map(int,input().split()))
    way = [[] for _ in range(100)]
    visit = [0]*100
    for i in range(N):
        a=target[i*2]
        b=target[i*2+1]
        way[a].append(b)
    start = 0
    end = 99
    print(f'#{tc} {tour(start)}')

# def solution(L, info, start_node, end_node, max_node):
#     graph = [[] for _ in range(max_node)]
#     for i in range(L):
#         A, B = info[2 * i], info[2 * i + 1]
#         graph[A].append(B)
#         visit = [0] * max_node
#         visit[start_node] = 1
#     ls = [start_node]
#     while ls:
#         node = ls.pop()
#         for next_node in graph[node]:
#             if not visit[next_node]:
#                 visit[next_node] = 1
#                 ls.append(next_node)
#     return visit[end_node]

# T = 10
# start_node = 0
# end_node = 99
# max_node = 100
# result = list()
# for _ in range(T):
#     tc, L = map(int, input().split())
#     info = list(map(int, input().split()))
#     result.append(f'#{tc} {solution(L, info, start_node, end_node, max_node)}')
# print('\n'.join(result))