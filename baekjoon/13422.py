# N : 집의 개수, M : 연속으로 훔칠 집의 개수, K: 방범장치 최소 돈의 양
# 1<= M <= N <= 100000
# 1<= K <= 1000000000
import sys
input = sys.stdin.readline

def solution(N:int,M:int,K:int,moneyList:list[int])->int:
    cnt,total = 0,sum(moneyList[0:M])
    if total < K: cnt += 1
    if N==M: return cnt
    s,e = 0,M%N
    for _ in range(N-1):
        total -= moneyList[s]
        s += 1
        total += moneyList[e]
        e = (e+1)%N
        if total < K:cnt+=1
    return cnt

T = int(input())
ans = list()
for tc in range(T):
    N,M,K = map(int,input().split())
    moneyList = list(map(int,input().split()))
    ans.append(solution(N,M,K,moneyList))
print(*ans)
