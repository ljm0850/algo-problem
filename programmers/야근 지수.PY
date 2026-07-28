def solution(n, works):
    cntDict  = {}
    max_cnt = max(works)
    for work in works:
        cntDict[work] = cntDict.get(work,0) + 1

    while n and max_cnt > 0:
        cnt = cntDict.get(max_cnt,0)
        if n >= cnt:
            n -= cnt
            cntDict[max_cnt] = 0
            max_cnt -= 1
            cntDict[max_cnt] = cntDict.get(max_cnt,0) + cnt
        else:
            cntDict[max_cnt] -= n
            cntDict[max_cnt-1] = cntDict.get(max_cnt-1,0) + n
            break

    answer = 0
    for i in range(1,max_cnt+1):
        answer += cntDict.get(i,0)*(i**2)

    return answer
