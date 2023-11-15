N = int(input())                                                        # N:1이상1000이하
container=[]
total = 0
for _ in range(N):
    L,H = map(int,input().split())                                      # L,H:1이상 1000이하
    container.append([L,H])
for i in range(N-1,-1,-1):                                              #L 기준 정렬
    for j in range(i):
        if container[j][0] > container[j+1][0]:
            container[j],container[j+1] = container[j+1],container[j]
max_H= 0
nowh=container[0][1]
for h in range(N):
    if container[h][1] > max_H:                                         #최대값 찾기
        max_H = container[h][1]
        max_L = container[h][0]

for k in range(N-1):
    if container[k][0] < max_L:                                         #최대값 도달 전까진 높이 갱신하며 면적 구하기
        if container[k][1] <= nowh:
            total += (container[k+1][0]-container[k][0])*nowh
        else:
            nowh = container[k][1]
            total += (container[k + 1][0] - container[k][0]) * nowh
    elif container[k][0] == max_L:                                      #최대값 도달시
        total += max_H
        max_H = 0
        for h in range(k+1,N):                                          #최대값 다시찾기
            if container[h][1] > max_H:
                max_H = container[h][1]
                max_L = container[h][0]
        nowh = max_H
        total += (container[k + 1][0] - container[k][0]-1) * nowh
total += container[-1][1]                                               # k범위를 N-2까지 잡아서 마지막만 따로 처리
print(total)