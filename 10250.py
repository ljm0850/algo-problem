T = int(input())

for tc in range(1,T+1):
    H,W,N = map(int,input().split())            # H = 층수, W = 층별 방수, N = 찾고자 하는 손님의 방
    floor = str(N % H)
    if floor == '0':
        floor = str(H)
    temp = N // H
    if N % H != 0:
        temp += 1
    if temp < 10:
        room = '0'+str(temp)
    else:
        room = str(temp)
    print(floor+room)

