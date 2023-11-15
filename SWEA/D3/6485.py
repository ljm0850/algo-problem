import sys
sys.stdin=open('s_input.txt')

#5000개의 버스정류장 1~5000까지 번호 붙음
#버스 노선 N개, i번째 버스 노선은 번호가 Ai이상,Bi이하인 모든 정류장만을  다니는 버스 노선

T= int(input())
for tc in range(1,T+1):
    N= int(input())                             #버스 노선수
    way = [list(map(int,input().split())) for _ in range(N)]#버스 노선, [A,B] A부터 B까지 정류장을 감
    P= int(input())                                         #버스 정류장의 수 1이상 500이하
    C =[int(input()) for _ in range(P)]                     #버스 정류장 번호 1이상 5000이하
    busstop = [0] * 5001                                    #5000번째 정류장을 만들기 위해

    for i in range(N):
        for j in range(way[i][0],way[i][1]+1): #버스가 지나가면 정류장에 1씩 카운트
            busstop[j] += 1
    print(f'#{tc}',end=' ')
    for p in range(P):        #알고자 하는 정류장 번호 검색
        print(busstop[C[p]],end=' ')
    print()