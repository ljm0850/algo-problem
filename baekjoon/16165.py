N,M = map(int,input().split())
teamSearch = dict()
memberSearch = dict()
for _ in range(N):
    teamName = input()
    memberSearch[teamName] = list()
    T = int(input())
    for __ in range(T):
        name = input()
        memberSearch[teamName].append(name)
        teamSearch[name] = teamName
    memberSearch[teamName].sort()
ans = list()
for _ in range(M):
    problem = input()
    problemType = int(input())
    if problemType == 0:
        print(*memberSearch[problem],sep='\n')
    else:
        print(teamSearch[problem])