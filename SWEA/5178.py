import sys
sys.stdin = open('sample_input.txt')

def sum_tree(ls,n):
    if ls[n] :
        return ls[n]
    else:
        if 2*n+1 <=N:
            ls[n] = sum_tree(ls,2*n)+sum_tree(ls,2*n+1)
        else:
            ls[n] = sum_tree(ls,2*n)
        return ls[n]

T= int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())                # N개의 노드, 리프 노드의 개수 M, 출력할 노드 번호 L
    tree = [0] * (N + 1)
    for _ in range(M):
        i,v = map(int,input().split())
        tree[i] = v
    print(f'#{tc} {sum_tree(tree,L)}')

