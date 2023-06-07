# pypy에서만 통과, python에서 통과시키려면 parent를 한단계만 하지 말고, 조부모, 증조부모... 까지 기록해야 할듯?
from collections import deque
import sys
input = sys.stdin.readline

def make_depth_parent(N:int,root:int)->tuple[list[int],list[int]]:
    global graph
    depth = [0]*(N+1)
    parent = [0]*(N+1)
    visited = [False]*(N+1)ㄷ
    visited[root] = True
    que = deque()
    que.append(root)
    cnt = 0
    while que:
        cnt += 1
        for _ in range(len(que)):
            now_node = que.popleft()
            for next_node in graph[now_node]:
                if not visited[next_node]:
                    que.append(next_node)
                    visited[next_node] = True
                    depth[next_node] = cnt
                    parent[next_node] = now_node
    return depth,parent

def solution(a:int,b:int)->int:
    global depth,parent
    # a는 b보다 깊거나 같음
    if check.get((a,b)):
        return check[(a,b)]

    a_path,b_path = [a],[b]
    while depth[a] != depth[b]:
        a = parent[a]
        a_path.append(a)

    while a != b:
        a = parent[a]
        b = parent[b]
        a_path.append(a)
        b_path.append(b)
        if check.get((a,b)):
            record_path(a_path,b_path,check[(a,b)])
            return check[(a,b)]
    record_path(a_path,b_path,a)
    return a

def record_path(A:list[int],B:list[int],value:int)->None:
    global check
    for a in A:
        for b in B:
            if depth[a] >= depth[b]:
                check[(a,b)] = value
            else:
                check[(b,a)] = value

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
depth,parent = make_depth_parent(N,1)
check = dict()

M = int(input())
for _ in range(M):
    a,b = map(int,input().split())
    if depth[a] >= depth[b]:
        ans = solution(a,b)
    else:
        ans = solution(b,a)
    print(ans)
