import sys
def dijkstra():
    # 모든 번호에 대한 최단거리 찾아야 하므로
    for _ in range(V):
        minlength = INF
        select = 0
        # 방문한 적은 없고, 가장 짧은 길이를 가진곳 찾기
        for i in range(1, V + 1):
            if not visited[i] and sol[i] < minlength:
                minlength = sol[i]
                select = i
        visited[select] = 1                                 # 선택된 곳 방문 처리

        for i in range(len(gra[select])):                   # 선택한 위치에서 graph 탐색
            next = gra[select][i][0]                        # 그래프로 연결될 수 있는 장소
            temp = sol[select] + gra[select][i][1]          # 현재 경로를 이용하면 next 까지 거리

            if sol[next] > temp:                            # 기존에 저장된 경로보다 짧으면 변경
                sol[next] = temp

V,E = map(int,sys.stdin.readline().split())      # V = 정점의 개수, E = 간선의 개수
K = int(sys.stdin.readline())                    # 시작 번호
gra = [[] for _ in range(V+1)]      # 노선 기록용
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    gra[u].append((v,w))

INF = 10000000                      # 문제에서 도달할 수 없는 높은 값
sol = [INF for _ in range(V+1)]     # 최단거리 저장용, 문제에서는 K부터 시작하므로 1차원
visited = [0]*(V+1)                 # 무한루프 방지
sol[K] = 0                          # 시작점의 최단거리는 0
dijkstra()

for i in range(1,V+1):
    t = sol[i]
    if t == INF:
        print('INF')
    else:
        print(t)
