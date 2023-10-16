import sys
input = sys.stdin.readline
def solution(N:int,M:int,P:int,arr:list[list[int]])->int:
    for ls in arr:
        ls.sort()

    for building in arr:
        cnt = 0
        for enemy in building:
            if enemy == -1:
                cnt += 1
                continue
            if enemy <= P:
                P += enemy
            else:
                while cnt and (enemy > P):
                    cnt -= 1
                    P *= 2
                if enemy <= P:
                    P += enemy
                else:
                    return 0
        P *= 2**(cnt)
    return 1

N,M,P = map(int,input().split())
total = [list(map(int,input().split())) for _ in range(N)]
ans = solution(N,M,P,total)
print(ans)