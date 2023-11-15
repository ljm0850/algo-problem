def solution(target:str)->int:
    ls = [(0,len(target)-1,0)]
    while ls:
        s,e,cnt = ls.pop()
        if s >= e:
            return cnt
        if target[s] == target[e]:
            ls.append((s+1,e-1,cnt))
        elif cnt == 0:
            ls.append((s+1,e,1))
            ls.append((s,e-1,1))
    return 2

T = int(input())
for _ in range(T):
    target = input().rstrip()
    ans = solution(target)
    print(ans)