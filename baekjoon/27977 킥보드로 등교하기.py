def solution(end:int,cnt:int)->int:
    s,e = 0,end
    while s < e:
        mid = (s+e) // 2
        value = check(mid,end,cnt)
        if value:
            e = mid
        else:
            s = mid + 1
    return e

def check(l:int,end:int,cnt:int)->bool:
    now = l
    visit = set()
    C = 0
    while now < end:
        if now in stations and not now in visit:
            visit.add(now)
            C += 1
            if C > cnt:
                return False
            now += l
            continue
        elif now in visit:
            return False
        else:
            now -= 1
            if now < 0:
                return False
    return True

L,N,K = map(int,input().split())
stations = set(map(int,input().split()))
ans = solution(L,K)
print(ans)