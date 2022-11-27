import sys
import heapq
ans = list()
# N은 문제의 수, M은 조건의 수
N,M = map(int,sys.stdin.readline().split())
problems = []
condition = [0 for _ in range(N+1)] # 남아 있는 조건의 수
check = [[] for _ in range(N+1)]  # 해당 key를 먼저 풀면 좋은 문제들이 들어감
for _ in range(M):
    A,B = map(int,sys.stdin.readline().split())
    check[A].append(B)
    condition[B] += 1

for i in range(1,N+1):
    key = condition[i]
    if not key:
        problems.append(i)

while problems:
    solved_problem = heapq.heappop(problems)
    ans.append(solved_problem)
    pbs = check[solved_problem]
    for pb in pbs:
        condition[pb] -= 1
        if condition[pb] == 0:
            heapq.heappush(problems,pb)
print(*ans)