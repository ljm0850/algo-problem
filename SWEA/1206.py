import sys
sys.stdin=open('input.txt')

for tc in range(1,11):
    T=int(input())
    tg=list(map(int,input().split()))
    total = 0
    for i in range(2,T-2):
        ls=[]
        ls += tg[i-2],tg[i-1],tg[i],tg[i+1],tg[i+2] #앞뒤 2개까지 높이 리스트 형성

        maximum1=ls[0]
        for j in ls: #리스트에서 제일 큰값 찾기
            if maximum1 < j:
                maximum1 = j
        ls.remove(maximum1) # 두번쨰로 큰 값을 찾기위해 maximum1값 제외

        maximum2 =ls[0]
        for jj in ls: #두번째로 큰 값 측정
            if maximum2 < jj:
                maximum2 =jj

        if tg[i] == maximum1: #주변에서 제일 높으면 높이 차를 total에 합산
            total += (maximum1-maximum2)
    print(f'#{tc} {total}')