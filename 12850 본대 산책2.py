# 0 : 정보과학관, 1 : 전산관, 2: 미래관, 3:신양관, 4:한경직기념관, 5: 진리관, 6:학생회관, 7 : 형남공학관
graph = [[1,2],[0,2,3],[0,1,3,4],[1,2,4,5],[2,3,5,7],[3,4,6],[5,7],[4,6]]

def solve(s,e,d):
    if check.get((s,e,d)):
        return check[(s,e,d)]
    if d <= 1:
        return 0
    m = d//2
    m2 = m +1 if d % 2 else m
    temp = 0
    for i in range(8):
        temp = (temp + solve(s,i,m) * solve(i,e,m2))%mod
    check[(s,e,d)] = temp
    return temp

mod = 1000000007
D = int(input())
check = {}
for i in range(8):
    for p in graph[i]:
        check[(i,p,1)] = 1

ans = solve(0,0,D)
print(ans)