import sys
sys.stdin=open('input (1).txt')

for tc in range(1,11):
    V,E = map(int,input().split())                  # V= 정점의  수(5이상 1000이하), E=간선의 수
    target = list(map(int,input().split()))
    temp = [[] for _ in range(V+1)]
    visit = [0] * (V+1)
    solve = []                  #작업순서 기록

    for i in range(E):
        temp[target[2*i+1]].append(target[2*i])
    s = 0
    while True:
        if visit[s] :           #했던 작업이면 다음 작업으로 이동
            pass
        elif not temp[s]:         #조건이 없다면
            visit[s] = 1        #작업 한것을 체크
            solve.append(s)     #작업 순서 기록
        else :                  #조건이 있다면
            for i in temp[s]:
                if visit[i] != 1:   #조건 미달성시 다음작업으로
                    break
            else:
                visit[s] = 1      #조건 달성시 체크
                solve.append(s)
        s += 1
        if s == V+1:                #새로운 사이클 가동용
            s = 1
        if visit == [1]*(V+1) :     #작업이 끝나면 반복문 종료
            break
    solve.pop(0)
    print(f'#{tc}',*solve)