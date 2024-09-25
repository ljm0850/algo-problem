def solution(n:int,value:list[list[str]])->list[str]:
    total = list()
    name = dict()
    for me in range(n):
        name[me] = value[me][0]
        for idx in range(n):
            if value[me][idx] == 'N':
                total.append([(n+me-idx)%n,me])
    ls = list()
    if total:
        for a,b in total:
            ls.append(f"{name[a]} was nasty about {name[b]}")
    else:
        ls.append("Nobody was nasty")
    return ls

tc = 0
while True:
    n = int(input())
    tc += 1
    if n == 0:
        break
    value = [input().split() for _ in range(n)]
    ans = solution(n,value)
    print(f'Group {tc}')
    print(*ans,sep="\n")
    print()