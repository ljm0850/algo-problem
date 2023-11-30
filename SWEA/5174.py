import sys
sys.stdin = open('sample_input.txt')

T= int(input())

for tc in range(1,T+1):
    E,N = map(int,input().split())              # E = 간선의 수 , N을 root로 하는 subtree 노드 개수 파악
    edge = list(map(int,input().split()))
    ch = [[] for _ in range(E+2)]               # 노드 번호는 1번부터 E+1번 까지 존재


    for i in range(E):
        ch[edge[i*2]].append(edge[i*2+1])
    stack =[N]
    cnt = 0
    while stack:                                #
        cnt +=1
        t = stack.pop()
        for j in ch[t]:
            stack.append(j)                     # 자손들을 스택에 추가
    print(f'#{tc} {cnt}')