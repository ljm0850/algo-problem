def solution(cnt,value):
    if cnt == 0:
        global ans
        ans += 1
        return
    for i in range(N):
        if not check[i]:
            newValue = value + kits[i] - K
            if newValue >= 0:
                check[i] = True
                solution(cnt-1,newValue)
                check[i] = False

N,K = map(int,input().split())
kits = list(map(int,input().split()))
check = [False]*(N)
ans = 0
solution(N,0)
print(ans)
