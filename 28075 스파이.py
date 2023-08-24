def make_task_idx()->list[tuple[int]]:
    task_idx = list()
    for r in range(2):
        for c in range(3):
            task_idx.append((r,c))
    return task_idx

def recur(endDay:int,day:int,beforePosition:int,total:int)->int:
    global task_idx,values,M
    if total >= M:
        return 6**(endDay-day)
    if day == endDay:
        return 0

    v = 0
    for task,position in task_idx:
        if beforePosition == position:
            ntotal = total + values[task][position]//2
        else:
            ntotal = total + values[task][position]
        v += recur(endDay,day+1,position,ntotal)
    return v

N,M = map(int,input().split())
values = [tuple(map(int,input().split())) for _ in range(2)]
task_idx = make_task_idx()
ans = recur(N,0,-1,0)
print(ans)