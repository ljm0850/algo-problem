def solution(N:int,sol:list[int])->tuple[int]:
    bestPH = 3000000000
    for i in range(N-2):
        if bestPH == 0:
            break
        s,e = i+1,N-1
        while s<e:
            total = sol[i] + sol[s] + sol[e]
            absTotal = abs(total)
            if bestPH > absTotal:
                bestPH = absTotal
                value = (i,s,e)
            if total > 0:
                e -= 1
            else:
                s += 1
    return (sol[value[0]],sol[value[1]],sol[value[2]])

N = int(input())
sol = sorted(list(map(int,input().split())))
ans = solution(N,sol)
print(*ans)