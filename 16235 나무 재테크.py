from collections import deque
import sys
input = sys.stdin.readline
def spring_summer():
    for r in range(N):
        for c in range(N):
            if not forest[r][c]:
                continue
            temp = {}
            nutrient = 0
            flag = False
            for age in range(len(forest_check[r][c])):
                tree_age = forest_check[r][c].popleft()
                cnt = forest[r][c][tree_age]
                if flag:
                    nutrient += (tree_age // 2) * cnt
                    continue
                total = tree_age * cnt
                if ground[r][c] >= total:
                    ground[r][c] -= total
                    temp[tree_age+1] = cnt
                    forest_check[r][c].append(tree_age+1)
                else:
                    flag = True
                    value = ground[r][c] // tree_age
                    if value:
                        ground[r][c] -= tree_age * value
                        temp[tree_age+1] = value
                        forest_check[r][c].append(tree_age+1)
                    nutrient += (tree_age // 2) * (cnt - value)
            ground[r][c] += nutrient
            forest[r][c] = temp

def fall():
    total = {}
    for r in range(N):
        for c in range(N):
            for tree in forest[r][c]:
                if tree % 5 == 0:
                    total[(r,c)] = total.get((r,c),0) + forest[r][c][tree]

    for P,V in total.items():
        r,c = P
        for d in range(8):
            nr,nc = r + dr[d], c + dc[d]
            if 0<=nr<N and 0<=nc<N:
                if forest[nr][nc].get(1):
                    forest[nr][nc][1] += V
                else:
                    forest[nr][nc][1] = V
                    forest_check[nr][nc].appendleft(1)
def winter():
    for r in range(N):
        for c in range(N):
            ground[r][c] += nutrients[r][c]

N,M,K = map(int,input().split())
ground = [[5]*N for _ in range(N)]
forest = [[{} for _ in range(N)] for __ in range(N)]
forest_check = [[[] for _ in range(N)] for __ in range(N)]
nutrients = [list(map(int,input().split())) for _ in range(N)]
dr,dc = (-1,-1,-1,0,0,1,1,1),(-1,0,1,-1,1,-1,0,1)
for _ in range(M):
    r,c,z = map(int,input().split())
    if forest[r-1][c-1].get(z):
        forest[r-1][c-1][z] += 1
    else:
        forest[r-1][c-1][z] = 1
        forest_check[r-1][c-1].append(z)

for r in range(N):
    for c in range(N):
        forest_check[r][c] = deque(sorted(forest_check[r][c]))

for _ in range(K):
    spring_summer()
    fall()
    winter()
ans = 0
for r in range(N):
    for c in range(N):
        ans += sum(forest[r][c].values())
print(ans)