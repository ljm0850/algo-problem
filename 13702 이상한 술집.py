import sys
input = sys.stdin.readline
def solution(K:int,drinks:list[int])->int:
    s,e = 1,max(drinks)
    value = 0
    while s <= e:
        mid = (s+e) // 2
        cnt = 0
        for drink in drinks:
            cnt += drink // mid
        if cnt >= K:
            s = mid + 1
            value = mid
        else:
            e = mid - 1
    return value

N,K = map(int,input().split())
drinks = [int(input()) for _ in range(N)]
ans = solution(K,drinks)
print(ans)