import sys
from collections import deque
def solve():
    ans = 0
    check = [False] * (n + 1)
    for i in range(1,n+1):
        if check[i] or choice[i] == i: continue
        j = i
        path = deque()
        path.append(j)

        while True:
            if not check[j] :
                check[j] = True
                if j != choice[j]:
                    j = choice[j]
                    path.append(j)
                else:
                    ans += len(path)-1
                    break
            elif j == i:
                break
            else:
                cnt = 0
                while path[0] != j:
                    path.popleft()
                    cnt += 1
                ans += cnt
                break
    return ans

T = int(sys.stdin.readline())
for tc in range(T):
    n = int(sys.stdin.readline())
    choice = [0]+list(map(int,sys.stdin.readline().split()))
    answer = solve()
    print(answer)
