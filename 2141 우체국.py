import sys
input = sys.stdin.readline

def solution(total:int,village:list[int],village_cnt:dict)->int:
    village.sort()
    people = 0
    value = total/2
    for idx in village:
        people += village_cnt[idx]
        if people >= value:
            return idx

N = int(input())
village,village_cnt=list(),dict()
total = 0

for _ in range(N):
    idx,cnt = map(int,input().split())
    total += cnt
    village.append(idx)
    village_cnt[idx] = cnt
ans = solution(total,village,village_cnt)
print(ans)