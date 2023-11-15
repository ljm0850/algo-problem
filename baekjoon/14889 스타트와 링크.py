import sys
def solve(A_team,B_team,a,b):
    global ans
    index = a+b
    if index < N:
        if a<n:
            solve(A_team+[index],B_team,a+1,b)
        if b<n:
            solve(A_team,B_team+[index],a,b+1)
    else:
        A_power,B_power = 0,0
        for A1 in A_team:
            for A2 in A_team:
                A_power += teamwork[A1][A2]
        for B1 in B_team:
            for B2 in B_team:
                B_power += teamwork[B1][B2]
        balance = abs(A_power - B_power)
        if ans > balance:
            ans = balance

N = int(sys.stdin.readline())
n = N//2
teamwork = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = 10000
solve([],[],0,0)
print(ans)
