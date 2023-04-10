def solution(R:int,room:list[int])->tuple[int]:
    room.sort()
    value = 0
    for idx in range(R-1):
        value = max(value,room[idx+1]-room[idx])
    return (room[R-1],room[0],value)

K = int(input())
for X in range(1,K+1):
    T = list(map(int,input().split()))
    room = T[1:]
    ans = solution(T[0],room)
    print(f'Class {X}')
    print(f'Max {ans[0]}, Min {ans[1]}, Largest gap {ans[2]}')