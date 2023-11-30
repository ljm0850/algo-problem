#인원은 최대 100명
#빈 번호 존재
def solve(x):
    global visit
    visit[x] = 1
    que = [x]
    que_temp = []
    sol = [x]
    while que :
        t = que.pop(0)
        if ch[t]:
            for i in ch[t]:
                if not visit[i]:
                    visit[i] = 1
                    que_temp.append(i)
        if not que and que_temp:            # 한 세대? 순서? 마다 que에 값을 넘겨주기 위하여 설계
            sol = []
            for j in que_temp:              # sol = que_temp , que_temp 값을 초기화 해야 하므로 마지막 que_temp 저장용
                sol.append(j)
            for _ in que_temp:              # 다음 세대? 순서?를 que에 넘겨줌
                que.append(_)
            que_temp.clear()
    return sol


for tc in range(1,11):
    ch = [[] for _ in range(101)]                   #index -> value 연결
    n,s = map(int,input().split())
    edge = list(map(int,input().split()))
    visit = [0] * 101
    for i in range(n//2):
        ch[edge[i*2]].append(edge[i*2+1])
    print(f'#{tc} {max(solve(s))}')
    