def move_cloud(d,s,N,cloud):
    after_cloud = set()
    for r,c in cloud:
        nr,nc = (N+r+dr[d]*(s%N))%N, (N+c+dc[d]*(s%N))%N
        after_cloud.add((nr,nc))
    return after_cloud
    
def raining_and_copy(cloud,N,buckets):
    temp = dict()
    dr,dc = (1,1,-1,-1),(1,-1,1,-1)
    for r,c in cloud:
        buckets[r][c] += 1
    for r,c in cloud:
        cnt = 0
        for d in range(4):
            nr,nc = r+dr[d], c+dc[d]
            if 0<=nr<N and 0<=nc<N and buckets[nr][nc]: # 매번 대각선 좌표 확인하는 거 보다 기록해두고 쓰는게 더 좋긴 할거 같다
                cnt += 1
        temp[(r,c)] = cnt
    for r,c in temp:
        buckets[r][c] += temp[(r,c)]

def new_cloud(before,N,buckets):
    cloud = set()
    for r in range(N):
        for c in range(N):
            if (r,c) in before:
                continue
            if buckets[r][c] >= 2:
                buckets[r][c] -= 2
                cloud.add((r,c))
    return cloud

N,M = map(int,input().split())
buckets = [list(map(int,input().split())) for _ in range(N)]
cloud = set()

for i in range(1,3):
    cloud.add((N-i,0))
    cloud.add((N-i,1))
dr,dc = (0,0,-1,-1,-1,0,1,1,1),(0,-1,-1,0,1,1,1,0,-1)
for _ in range(M):
    d,s = map(int,input().split())
    cloud = move_cloud(d,s,N,cloud)
    raining_and_copy(cloud,N,buckets)
    cloud = new_cloud(cloud,N,buckets)
ans = 0
for i in range(N):
    ans += sum(buckets[i])
print(ans)