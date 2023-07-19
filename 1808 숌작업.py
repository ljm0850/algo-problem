def redefine_levels(node:int,h:int)->None:
    global levels
    levels[node] = h
    for child in children[node]:
        redefine_levels(child,h+1)

def works(P_node:int,C_node:int)->int:
    global parents,children
    children[P_node].add(C_node)
    children[parents[C_node]].remove(C_node)
    parents[C_node] = P_node
    gap = levels[C_node] - levels[P_node] - 1
    redefine_levels(P_node,levels[P_node])
    return gap

def find_max_idx(ls:list[int])->int:
    value,idx = 0,0
    for i in range(len(ls)):
        if value < ls[i]:
            value = ls[i]
            idx = i
    return idx

def solution(H:int)->int:
    cnt = 0
    while True:
        global levels
        target = find_max_idx(levels)
        if levels[target] > H:
            gap = levels[target]-H
            C_node = target
            h = min(2,H+1)
            while (levels[C_node] > h):
                C_node = parents[C_node]

            if levels[C_node] > H:
                P_node = C_node
                for _ in range(gap+1):
                    P_node = parents[P_node]
            else:
                P_node = 0
            cnt += works(P_node,C_node)
        else:
            return cnt

N = int(input())
parents = [0]*(N)   # 부모노드 저장
children = [set() for _ in range(N)]   #자식노드 저장
levels = [0]*(N)
for _ in range(N-1):
    a,b = map(int,input().split())
    parents[b] = a
    children[a].add(b)
redefine_levels(0,0)
H = int(input())
ans = solution(H)
print(ans)
