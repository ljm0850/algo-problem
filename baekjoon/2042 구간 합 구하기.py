import sys
# 트리 값 업데이트
def change_tree(idx:int,gap:int,tree:list[int],N)->None:
    while idx <= N:
        tree[idx] += gap
        idx += idx & -idx
    return tree

# 1 해당 idx까지의 합 조회
def sum_range(idx:int)->int:
    total = 0
    while idx:
        total += tree[idx]
        idx -= idx & -idx
    return total

N,M,K = map(int,sys.stdin.readline().split())
# 바이너리 트리
tree = [0]*(N+1)
for idx in range(1,N+1):
    num = int(sys.stdin.readline())
    tree = change_tree(idx,num,tree,N)
for _ in  range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        before = sum_range(b)-sum_range(b-1)
        gap = c - before
        change_tree(b,gap,tree,N)
    elif a == 2:
        print(sum_range(c)-sum_range(b-1))
