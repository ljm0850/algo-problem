def solution(N:int,cmds:str)->int:
    idx,cnt = 0,0
    for idx in range(N):
        if cmds[idx] =='W' and cmds[idx-1] == 'E': cnt += 1
    return cnt

N = int(input())
cmds = input()
ans = solution(N,cmds)
print(ans)