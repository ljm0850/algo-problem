def solution(X:int,Y:int)->int:
    Z = (100*Y) // X
    if Z >= 99:
        return -1
    s,e = 0,X
    value = X
    while s<=e:
        m = (s+e) // 2
        new_Z = (100*(Y+m))//(X+m)
        if new_Z > Z:
            e = m - 1
            value = m
        else:
            s = m + 1
    return value

X,Y = map(int,input().split())
ans = solution(X,Y)
print(ans)