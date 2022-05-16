from collections import deque
def solve():
    ans_cnt,ans_way = 0,0
    if N==K:
        print(0)
        print(1)
        return
    visited = [0]*100001
    visited[N] = 1
    que = deque()
    que.append(N)
    cnt = 0
    while not ans_cnt:
        cnt += 1
        temp = []
        for l in range(len(que)):
            now = que.popleft()
            for next in (now-1,now+1,2*now):
                if 0<=next<=100000 and not visited[next]:
                    if next ==  K:
                        ans_cnt = cnt
                        ans_way += 1
                    else:
                        temp.append(next)           # 방문처리를 한꺼번에 해주기 위해
                        que.append(next)
        for t in temp:                              # 방문처리
            visited[t] = 1
    print(ans_cnt)
    print(ans_way)
    return

N,K = map(int,input().split())
solve()
