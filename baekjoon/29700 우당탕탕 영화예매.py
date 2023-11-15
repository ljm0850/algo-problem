import sys
input = sys.stdin.readline

def solution(R:int,C:int,K:int,theater:list[list[int]])->int:
    if C < K:
        return 0
    ans = 0
    for r in range(R):
        value = 0
        for i in range(K):
            value += theater[r][i]
        if value == 0:
            ans += 1
        s = 0
        for e in range(K, C):
            value += theater[r][e]
            value -= theater[r][s]
            s += 1
            if value == 0:
                ans += 1
    return ans

R,C,K = map(int,input().split())
theater = [list(map(int,input().rstrip())) for _ in range(R)]
answer = solution(R,C,K,theater)
print(answer)