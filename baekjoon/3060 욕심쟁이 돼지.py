def solution(N:int,ls:list[int])->int:
    value = sum(ls)
    day = 1
    while N>=value:
        day +=1
        todayFeed = [0]*6
        value = 0
        for pig in range(6):
            todayFeed[pig] = ls[pig] + ls[(pig+1)%6] + ls[pig-1] + ls[(pig+3)%6]
            value += todayFeed[pig]
        ls = todayFeed
    return day

T = int(input())
for _ in range(T):
    N = int(input())
    total = list(map(int,input().split()))
    ans = solution(N,total)
    print(ans)