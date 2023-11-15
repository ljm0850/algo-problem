# def DFS(x):
#     global visted
#     visted[x] = 1
#     print(x,end=' ')
#     for i in ch[x]:
#         if not visted[i]:
#             DFS(i)
#
#
# def BFS(x):
#     global visted
#     visted[x] = 1
#     que = [x]
#     while que:
#         temp = que.pop(0)
#         print(temp, end=' ')
#         for i in ch[temp]:
#             if not visted[i]:
#                 que.append(i)
#                 visted[i] = 1
#
# N,M,V = map(int,input().split())
# ch = [[] for _ in range(N+1)]
# for i in range(M):
#     p,c = map(int,input().split())
#     ch[p].append(c)
#     ch[c].append(p)
# for j in ch:
#     j.sort()
# visted = [0]*(N+1)
# sol = []
# DFS(V)
# print()
# visted = [0]*(N+1)
# BFS(V)

def DFS(x):
    visit = [0]*(N+1)
    sol = []
    stack = [x]
    while stack:
        temp = stack.pop()
        if not visit[temp]:
            sol.append(temp)
            visit[temp] = 1
            for i in ch[temp][::-1]:
                    stack.append(i)
    return sol

def BFS(x):
    visit = [0]*(N+1)
    sol = []
    que = [x]
    while que:
        temp = que.pop(0)
        if not visit[temp]:
            sol.append(temp)
            visit[temp] = 1
            for i in ch[temp]:
                    que.append(i)
    return sol

N,M,V = map(int,input().split())
ch = [[] for _ in range(N+1)]
for i in range(M):
    p,c = map(int,input().split())
    ch[p].append(c)
    ch[c].append(p)
for j in ch:
    j.sort()
print(*DFS(V))
print(*BFS(V))
