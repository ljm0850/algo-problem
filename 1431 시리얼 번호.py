def solution(N:int,ls:list[str])->list[str]:
    # bubble sort
    cnt = {}
    for i in range(N):
        target = ls[i]
        temp = 0
        for t in target:
            if t.isdigit():
                temp += int(t)
        cnt[target] = temp

    for i in range(N-1,0,-1):
        for j in range(i):
            L,R = len(ls[j]),len(ls[j+1])
            if L > R:
                ls[j],ls[j+1] = ls[j+1],ls[j]
            elif L == R:
                L_cnt,R_cnt = cnt[ls[j]],cnt[ls[j+1]]
                if L_cnt > R_cnt:
                    ls[j],ls[j+1] = ls[j+1],ls[j]
                elif L_cnt == R_cnt:
                    if ls[j] > ls[j+1]:
                        ls[j],ls[j+1] = ls[j+1],ls[j]
    return ls

N = int(input())
ls = [input() for _ in range(N)]
sortedLs = solution(N,ls)
for alpha in sortedLs:
    print(alpha)