#예전에 푼거라 내장함수 사용이 있습니다
T = int(input())

for i in range(T):
    N,M = input().split()
    n=int(N)
    m=int(M)
    # 전체 숫자를 target 리스트로 변경
    target = []
    for j in range(n):
        target.append(list(map(int,input().split())))
    # x축을 m개 숫자의 합으로 변경하여 p1에 저장    
    p1=[]
    for k in range(n):
        p2=[]
        for l in range(n):
            p2.append(sum(target[k][l:l+m]))        
        p1.append(p2)
    # p1의 x,y축 바꾸기
    xyc = []
    for ii in range(len(p1)):
        b=[]
        for iii in range(len(p1)):
            b.append(p1[iii][ii])
        xyc.append(b)
    # 바뀐 x,y축에서 x축을 m개 숫자의 합으로 변경하여 p3에 저장
    solve =[]
    for k in range(len(xyc)):
        p3=[]
        for l in range(len(xyc)):
            p3.append(sum(xyc[k][l:l+m]))
        solve.append(p3)
    #p3값중 최고값 찾기
    high = max(solve[0])
    for ii in range(1,len(solve)):
        if high < max(solve[ii]) :
            high = max(solve[ii])
    print(f'#{i+1} {high}')
