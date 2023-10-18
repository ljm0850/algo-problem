import sys
input = sys.stdin.readline

N,M = map(int,input().split())
friends = [set() for i in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    friends[a].add(b)
    friends[b].add(a)

maxNum = 12000
ans = maxNum
for A in range(1,N+1):
    for B in friends[A]:
        for C in friends[B]:
            if C in friends[A]:
                ans = min(ans,len(friends[A]) + len(friends[B]) + len(friends[C]) - 6)
if ans != maxNum:
    print(ans)
else:
    print(-1)